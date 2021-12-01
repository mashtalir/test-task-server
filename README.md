<h1>Docker settings</h1>
<p>1) after pulling all the project move Dockerfile and runner.sh to directory above
<br> (take care of changing pathes inside Dockerfile)
</p>
<p>2) Inside of directory where Dockerfile is - run:
<br> docker build . -t "image_name"
<br> docker run -p 3000:3000 -p 8000:8000 "image_name or image_id"
</p>
<p>3) To reach webpage write localhost:3000 in browser</p>
<p>This is so stupid because i did 2 separate repositories for client and server and Dockerfile should be always<br>
  in directory above of project</p>



<h1>For Linux users</h1>
  <h2>Create virualenv and activate</h2>
    <p>python3 -m venv venv</p>
    <p>source ./venv/bin/activate</p>
   <h2>Install requirements</h2>
     <p>pip install -r requirements.txt</p>
   <h2>Run server</h2>
   <p>python3 manage.py runserver</p>
