import os
import re
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from generate_result_report.service.generate_result_report_service_impl import GenerateResultReportServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))


generateResultReportRouter = APIRouter()

async def injectGenerateResultReportService() -> GenerateResultReportServiceImpl:
    return GenerateResultReportServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@generateResultReportRouter.get('/generate-result-report-result')
async def requestGenerateResultReportResult(generateResultReportService: GenerateResultReportServiceImpl =
                                       Depends(injectGenerateResultReportService)):
    ColorPrinter.print_important_message("requestGenerateResultReportResult()")

    generatedResultReportResult = generateResultReportService.requestGenerateResultReportResult()

    return JSONResponse(content=generatedResultReportResult, status_code=status.HTTP_200_OK)
