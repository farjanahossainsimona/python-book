import sys
import os
print(type(sys.path))
print(len(sys.path))
print(sys.path)
for path in sys.path:
    print(path)
# sys.path.append('/home/simona')
# print(sys.path)
# print(os.getcwd)
# print(sys.executable)
# print(sys.platform)
# print(os.getcwd())
# print(os.chdir('/Users/SEU/Desktop/'))
# print(os.getcwd())
# print(os.mkdir('new_folder'))
# print(os.getcwd())
# print(os.makedirs('1/2/3/4/5'))
# print(os.rmdir(test))  # to remove folder from current working directory
#print(os.rename('new_folder', 'old_folder'))
print(os.path.basename('Users/SEU/Desktop/home/simona/test.py'))
print(os.getcwd())
print(os.path.dirname('/Users/SEU/Desktop/python-book'))
print(os.path.exists('/Users/SEU/Desktop/python-book'))
print(os.path.exists('Users/SEU/Desktop/home/simona/test.py'))
print(os.path.isdir('/Users/SEU/Desktop'))
print(os.path.isfile('/Users/SEU/Desktop/test.py'))
dir = os.getcwd()
print(dir)
print(os.path.join(dir, 'test.py'))
print(os.path.split('/Users/SEU/Desktop/python-book/test.py'))
print(os.system('uname -r'))
