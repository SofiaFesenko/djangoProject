import time
import uuid

from django.utils.deprecation import MiddlewareMixin
from utils.loggers import logger, LogLevels


class XProcessTimeMiddleware(MiddlewareMixin):
    async def __call__(self, request):
        start_time = time.monotonic()
        response = await self.get_response(request)
        process_time = time.monotonic() - start_time
        response["X-PROCESS-TIME"] = str(process_time)
        return response


class XRequestIDMiddleware(MiddlewareMixin):
    async def __call__(self, request):
        request_id = uuid.uuid1(node=None, clock_seq=None)
        request.request_id = request_id
        with logger.contextualize(request_id=request_id):
            response = await self.get_response(request)
        response["X-REQUEST-ID"] = str(request_id)
        return response


class HandleErrorsMiddleware(MiddlewareMixin):
    async def process_exception(self, request, exception):  # noqa
        import traceback
        traceback = str(traceback.format_exc())
        message = f"{request.path_info};\n{str(exception)};\n {traceback}"
        logger.log(LogLevels.MIDDLEWARE_ERROR_HANDLER, message)
