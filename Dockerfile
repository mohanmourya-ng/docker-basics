# Define the Base Image
FROM python:alpine3.21

# Setting up the Work directory 
WORKDIR /app 

# Copy the source code to work directory 
COPY . .

# install the dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000 

CMD ["python", "app.py"]