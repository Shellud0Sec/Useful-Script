import os
import argparse
import traceback
import uncompyle6

def decompile_pyc_files(dir_path, error_log_file):
    # 遍历文件夹下的所有文件和子文件夹
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # 如果是 pyc 文件，就执行反编译
            if file.endswith('.pyc'):
                pyc_file = os.path.join(root, file)
                py_file = os.path.splitext(pyc_file)[0] + '.py'
                try:
                    with open(py_file, 'w') as f:
                        uncompyle6.decompile_file(pyc_file, f)
                    print('Decompiled', pyc_file, 'to', py_file)
                except Exception as e:
                    # 记录反编译失败的文件名到日志文件中
                    with open(error_log_file, 'a') as f:
                        f.write(pyc_file + '\n')
                    print('Failed to decompile', pyc_file, ':', e)
                    traceback.print_exc()

        for dir in dirs:
            # 递归遍历子文件夹
            decompile_pyc_files(os.path.join(root, dir), error_log_file)

# 使用命令行参数指定要反编译的项目目录

// root/exploit-tools/python/pyc_decode/usr/local/var/www/html
parser = argparse.ArgumentParser()
parser.add_argument('dir_path', help='the directory path to decompile')
args = parser.parse_args()

# 记录反编译失败的文件名到日志文件中
error_log_file = 'error_pyc.log'
if os.path.exists(error_log_file):
    os.remove(error_log_file)

decompile_pyc_files(args.dir_path, error_log_file)
