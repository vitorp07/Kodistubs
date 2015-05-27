## @package xbmcvfs
#  Classes and functions to work with files and folders.
#

import os
import shutil

class File(object):
    def __init__(self, filename, mode=None):
        """
        'w' - opt open for write
        example:
         f = xbmcvfs.File(file, ['w'])
        """
        if mode == 'w':
            self._file = open(filename, mode='wb')
        else:
            self._file = open(filename, mode='rb')

    def close(self):
        """
        example:
         f = xbmcvfs.File(file)
         f.close()
        """
        self._file.close()

    def read(self, bytes=0):
        """
        bytes : how many bytes to read [opt]- if not set it will read the whole file
        example:
        f = xbmcvfs.File(file)
        b = f.read()
        f.close()
        """
        if not bytes:
            bytes = -1
        return self._file.read(bytes)

    def readBytes(self, numbytes=0):
        """
        readBytes(numbytes)

        numbytes : how many bytes to read [opt]- if not set it will read the whole file

        returns: bytearray

        example:
        f = xbmcvfs.File(file)
        b = f.read()
        f.close()
        """
        return bytearray(self.read(numbytes))

    def seek(self, seekBytes, iWhence):
        """
        FilePosition : position in the file
        Whence : where in a file to seek from[0 begining, 1 current , 2 end possition]
        example:
         f = xbmcvfs.File(file)
         result = f.seek(8129, 0)
         f.close()
        """
        self._file.seek(seekBytes, iWhence)

    def size(self):
        """
        example:
         f = xbmcvfs.File(file)
         s = f.size()
         f.close()
        """
        old_file_position = self._file.tell()
        self._file.seek(0, os.SEEK_END)
        size = self._file.tell()
        self._file.seek(old_file_position, os.SEEK_SET)
        return size

    def write(self, buffer):
        """
        buffer : buffer to write to file
        example:
         f = xbmcvfs.File(file, 'w', True)
         result = f.write(buffer)
         f.close()
        """
        self._file.write(buffer)


def copy(source, destination):
    """Copy file to destination, returns true/false.

    source: string - file to copy.
    destination: string - destination file

    Example:
        success = xbmcvfs.copy(source, destination)"""
    try:
        shutil.copy(source, destination)
        return True
    except IOError:
        return False


def delete(file):
    """Deletes a file.

    file: string - file to delete

    Example:
        xbmcvfs.delete(file)"""
    try:
        os.remove(file)
        return True
    except IOError:
        return False


def rename(file, newFileName):
    """Renames a file, returns true/false.

    file: string - file to rename
    newFileName: string - new filename, including the full path

    Example:
        success = xbmcvfs.rename(file,newFileName)"""
    try:
        os.rename(file, newFileName)
        return True
    except (OSError, IOError):
        return False


def mkdir(path):
    """Create a folder.

    path: folder

    Example:
        success = xbmcfvs.mkdir(path)
    """
    try:
        os.mkdir(path)
        return True
    except OSError:
        return False


def mkdirs(path):
    """
    mkdirs(path)--Create folder(s) - it will create all folders in the path.

    path : folder

    example:

    - success = xbmcvfs.mkdirs(path)
    """
    try:
        os.makedirs(path)
        return True
    except OSError:
        return False


def rmdir(path):
    """Remove a folder.

    path: folder

    Example:
        success = xbmcfvs.rmdir(path)
    """
    try:
        os.rmdir(path)
        return True
    except OSError:
        return False


def exists(path):
    """Checks for a file or folder existance, mimics Pythons os.path.exists()

    path: string - file or folder

    Example:
        success = xbmcvfs.exists(path)"""
    return os.path.exists(path)


def listdir(path):
    """
    listdir(path) -- lists content of a folder.

    path        : folder

    example:
     - dirs, files = xbmcvfs.listdir(path)
    """
    dirs = []
    files = []
    for item in os.listdir(path):
        if os.path.isdir(item):
            dirs.append(item)
        else:
            files.append(item)
    return dirs, files


class Stat(object):
    def __init__(self, path):
        """
        Stat(path) -- get file or file system status.

        path        : file or folder

        example:
        - print xbmcvfs.Stat(path).st_mtime()
        """

    def st_mode(self):
        return None

    def st_ino(self):
        return None

    def st_nlink(self):
        return None

    def st_uid(self):
        return None

    def st_gid(self):
        return None

    def st_size(self):
        return None

    def st_atime(self):
        return None

    def st_mtime(self):
        return None

    def st_ctime(self):
        return None
