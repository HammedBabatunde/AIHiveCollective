FROM python:3-alpine

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN python -m venv myenv

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
