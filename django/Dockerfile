FROM django2.1:latest

ENV APP_PATH /opt/apps

COPY . $APP_PATH/
RUN pip install --no-cache-dir -r $APP_PATH/requirements.txt
