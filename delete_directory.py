import shutil

dir_to_delete = "<directory to delete>"

shutil.rmtree(dir_to_delete)

print 'Deleted directory: ' + dir_to_delete