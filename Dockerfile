FROM python:3.9

#Set the working directory in the container

WORKDIR /app

#Copy the requirements file and install dependencies

COPY requirements.txt -/

RUN pip install-no-cache-direr requirements.txt

#Copy the rest of the application code

COPY app .

#Expose the port the app runs on

EXPOSE 8000

#Command to run the application

CMD ["uvicorn", "app.main: app", "host","0.0.0.0", "e-port","8000", "reload"]
