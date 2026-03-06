import traceback
from rembg import remove

try:
    in_path = r'D:\Python\download.jpg'
    out_path = r'D:\Python\download_no_bg.png'
    print('reading', in_path)
    with open(in_path, 'rb') as f:
        data = f.read()
    print('calling remove() (this may take a few seconds)')
    out = remove(data)
    print('writing', out_path)
    with open(out_path, 'wb') as f:
        f.write(out)
    print('done')
except Exception as e:
    print('error:', e)
    traceback.print_exc()
