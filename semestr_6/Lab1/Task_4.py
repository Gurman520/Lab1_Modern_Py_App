import shutil
from datetime import datetime


def make_reserve_arc(source, dest):
    now = datetime.now()
    now = now.strftime(r"%Y-%m-%d_%H;%M;%S")
    now = "archive_" + str(now)
    shutil.make_archive(dest+now, 'zip', root_dir=source)


What_to_take = "./1 OS/dir"
Where_to_put_it = "./"
make_reserve_arc(What_to_take, Where_to_put_it)
