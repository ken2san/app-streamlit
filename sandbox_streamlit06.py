import streamlit as st
import pandas as pd
from PIL import Image
from PIL import ImageDraw
import io
from google.cloud import vision


def detect_faces(file):
    #draw=ImageDraw.Draw(picture)
    picture=Image.open(file)
    with io.BytesIO() as output:
        picture.save(output,format="JPEG")
        content=output.getvalue()

    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    st.write('Faces:')

    for face in faces:
        st.write('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        st.write('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        st.write('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])
        st.write('face bounds: {}'.format(','.join(vertices)))
        draw=ImageDraw.Draw(picture)
        draw.rectangle([(face.bounding_poly.vertices[0].x,face.bounding_poly.vertices[0].y),(face.bounding_poly.vertices[2].x,face.bounding_poly.vertices[2].y)],fill=None,outline='green',width=5)
        st.image(picture,caption="Uploaded File",width=320)
        picture=Image.open(file)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

st.title("Face cognition")
upLoaded_file=st.file_uploader("Chooose an image...",type='jpg')

if upLoaded_file is not None:
  detect_faces(upLoaded_file)
    
    #with io.BytesIO() as output:
        #img.save(output,format="JPEG")
        #binary_img=output.getvalue()
        #verteces=detect_faces(pic)
        #draw=ImageDraw.Draw(pic)
        #st.write(verteces[0],verteces[2])
        #draw.rectangle([(verteces[0].x,verteces[0].y),(verteces[2].x,verteces[2].y)],fill=None,outline='green',width=5)
        #draw.rectangle([(45,0),(213,181)],fill=None,outline='green',width=5)
    
    
