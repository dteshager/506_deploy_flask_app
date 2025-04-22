
#Use official python image
FROM python:3.11-slim
#Set working directory in container
WORKDIR /app
#Copy req.txt file and install it.
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

#Copy the rest of the code
COPY . .

#Expose port
EXPOSE 5000
#command to run the python file.
CMD ["python", "app.py"]
