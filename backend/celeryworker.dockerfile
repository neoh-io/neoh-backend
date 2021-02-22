FROM python:3.8

COPY ./app /app
WORKDIR /app

ENV PYTHONPATH=/app

ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then python -m pip install -e \".[tests]\" ; else python -m pip install -e \".\"; fi"

COPY ./app/worker-start.sh /worker-start.sh

RUN chmod +x /worker-start.sh

CMD ["bash", "/worker-start.sh"]