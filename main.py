import os

cur_dir = os.getcwd() + '\\'


def get_vid_dirs(path=os.getcwd()) -> list:
    vid_dirs = []
    for path, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if '.mp4' in file or '.mkv' in file:
                vid_dirs.append(path)
                break
    return vid_dirs


def get_cover(_dir: str) -> str:
    for file in os.listdir(_dir):
        if ('.jpg' in file or '.png' in file or '.jpeg' in file) and 'cover' in file:
            return _dir.replace(cur_dir, '') + '\\' + file


def index_generator(dirs: list) -> str:
    innerHtml = ''
    for dir in dirs:
        series = dir.split('\\')[-1]
        cover = get_cover(dir)
        data = f'''
            <div class="vid-box">
                <div class="vid">
                    <a href= "{series}.html">
                        <img src="{cover}" alt="{series}">
                    </a>
                </div>

                <p class="vid-title">{series}</p>
            </div>
        '''
        innerHtml += data
    return innerHtml


Vid_dirs = get_vid_dirs()

index_html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
</head>

<body>
    <div class="home">
        <a href="index.html">
            Home
        </a>
    </div>

    <div class="container">
        <div class="vid-container">
           {index_generator(Vid_dirs)}
        </div>
    </div>


    <script src="script.js"></script>
</body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(index_html)


def gen_vid_page(src_folder: str) -> str:
    inner_html = ''
    for file in os.listdir(src_folder):
        if file.endswith('.mp4') or file.endswith('.mkv'):
            vid_file = src_folder.replace(cur_dir, '') + '\\' + file
            series = vid_file.split('\\')[-1].split('.')[:-1][0]
            vid_box = f'''
             <div class="vid-box">
                <div class="vid">
                <video src="{vid_file}" controls=true></video>
                </div>

                <p class="vid-title">{series}</p>
            </div>
            '''
            inner_html += vid_box
    return inner_html


def all_html_generator(vid_dirs: list) -> None:
    for vid_dir in vid_dirs:
        vid_html_name = (vid_dir.split('\\')[-1] + '.html')
        inner_html = gen_vid_page(vid_dir)
        html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Video</title>
            <link rel="stylesheet" href="style.css">
            <script src="script.js"></script>
        </head>

        <body>
            <div class="home">
                <a href="index.html">
                    Home
                </a>
            </div>

            <div class="container">
                <div class="vid-container">
                    {inner_html}
                </div>
            </div>

            <script src="script.js"></script>
        </body>
        </html>
        '''
        with open(vid_html_name, 'w') as g:
            g.write(html)


all_html_generator(Vid_dirs)
