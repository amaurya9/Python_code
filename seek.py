"""seek(...)
     |      Change stream position.
     |
     |      Change the stream position to the given byte offset. The offset is
     |      interpreted relative to the position indicated by whence.  Values
     |      for whence are:
     |
     |      * 0 -- start of stream (the default); offset should be zero or positive
     |      * 1 -- current stream position; offset may be negative
     |      * 2 -- end of stream; offset is usually negative'''
     |
     |      Return the new absolute position.
     |
     |  seekable(self, /)
     |      Return whether object supports random access.
     |
     |      If False, seek(), tell() and truncate() will raise UnsupportedOperation.
     |      This method may need to do a test seek()."""
