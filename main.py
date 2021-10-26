import datetime as dt
import glob
import os
import plistlib
import subprocess


JST = dt.timezone(dt.timedelta(hours=9))
UTC = dt.timezone(dt.timedelta(hours=0))


for path in sorted(glob.glob('input/**/*.m2ts')):
    output = f"{path.replace('input/', 'output/').replace('.m2ts', '')}.mp4"
    os.makedirs(os.path.dirname(output), exist_ok=True)
    modd_path = path + '.modd'
    metadata_string = ''
    ts = None
    data = {}
    if os.path.exists(modd_path):
        with open(modd_path, 'rb') as f:
            raw = plistlib.load(f, fmt=plistlib.FMT_XML)
            if len(raw['MetaDataList']) > 1:
                print('MetaDataListが2つ以上ある')
                raise
            meta = raw['MetaDataList'][0]
            ts = dt.datetime(1899, 12, 30, tzinfo=JST) + dt.timedelta(days=meta['DateTimeOriginal'])
            lat, lon = meta['Geolocation'].get('Latitude'), meta['Geolocation'].get('Longitude')
            data = {
                'creation_time': ts.astimezone(UTC).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'date': ts.isoformat(),
                'location': f'{lat:+}{lon:+}/' if lat is not None and lon is not None else None,
            }
    else:
        ts = dt.datetime.strptime(os.path.splitext(os.path.basename(path))[0], '%Y%m%d%H%M%S').replace(tzinfo=JST)
        data = {
            'creation_time': ts.astimezone(UTC).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'date': ts.isoformat(),
        }

    metadata_string = ' '.join([f'-metadata {k}="{v}"' for k, v in data.items() if v is not None])
    cmd = f'ffmpeg -y -i {path} {metadata_string} {output}'
    print('\n\ncall ------')
    print(cmd)
    subprocess.call(cmd, shell=True)
    if ts:
        cmd = f'touch -c -t {ts.astimezone(UTC).strftime("%Y%m%d%H%M.%S")} {output}'
        print(cmd)
        subprocess.call(cmd, shell=True)
