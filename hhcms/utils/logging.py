# PROJECT : hhcms
# TIME : 18-4-22 下午2:18
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from hhcms.utils import get_log_file
from logging import FileHandler as BaseFileHandler, StreamHandler


class FileHandler(BaseFileHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(filename='', mode='a', encoding=None, delay=False)

    def _open(self):
        self.baseFilename = get_log_file()
        return open(self.baseFilename, self.mode, encoding=self.encoding)

    def emit(self, record):
        """
        Emit a record.

        If the stream was not opened because 'delay' was specified in the
        constructor, open it before calling the superclass's emit.
        """
        if self.stream is None:
            self.stream = self._open()
        StreamHandler.emit(self, record)
        self.stream.close()
        self.stream = None
