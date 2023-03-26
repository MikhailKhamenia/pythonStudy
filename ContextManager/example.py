from Tools.scripts.fixcid import err


class FileWithHeadingAndEnd(object):
    def __enter__(self):

        foo = open("foo.txt", "w")
        foo.write("File Heading\n")
        print('Open')
        return foo

    def __exit__(self, exc_type, exc_val, exc_tb):
        foo.write('File End\n')
        foo.close()
        print('Closed')

with FileWithHeadingAndEnd() as foo:
   # Code Block
    i = 0
    while i<10:
        foo.write("Line: %s \n" % str(i))
        i += 1


import contextlib

@contextlib.contextmanager
def make_context():
    print('entering')
    try:
        fo = open("foo2.txt", "w")
        fo.write("File Heading\n")
        yield fo
    except (RuntimeError, err):
        print('ERROR:', err)
    finally:
        print('exiting')
        fo.write('File End\n');
        fo.close()

with make_context() as fo:
    i = 0
    while i<10:
        fo.write("Line: %s \n" % str(i))
        i += 1