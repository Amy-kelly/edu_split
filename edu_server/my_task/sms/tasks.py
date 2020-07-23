from edu_server.settings import constants
from my_task.main import app
import logging

from edu_server.utils.send_msg import Message

logger = logging.getLogger('django')
#name指定当前任务名称
@app.task(name="send_sms")
def send_sms(mobile,code):
    print("短信发送")
    message = Message(constants.API_KEY)
    status = message.send_message(mobile,code)
    if not status:
        logger.error("短信发送失败，手机号为：%s" % mobile)
    return "message"