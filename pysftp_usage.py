import pysftp

host='172.21.0.0'
port=22
username='test_user'
password='qwerty123!'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

# copy test file, to the remote server
with pysftp.Connection(host=host, username=username, password=password, port=port, cnopts=cnopts) as sftp:
    local_path = "test_file.txt"
    remote_path = "/test_folder/test_file.txt"
    sftp.put(local_path, remote_path)
    sftp.close()
    print('Success')
