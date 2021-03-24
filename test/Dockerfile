FROM python:3.7
RUN pip install pipenv
COPY . /app
WORKDIR /app
RUN if [ ! -f "Pipfile.lock" ] ; then pipenv lock ; else echo Pipfile.lock exists ; fi
RUN pipenv sync
RUN pipenv install --dev
CMD tail -f /dev/null