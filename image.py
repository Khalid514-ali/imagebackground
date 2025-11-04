from rembg import remove
import streamlit as st

SUPPORTED_FILE_TYPES=['.png','.jpg','.jpeg']
def main():
    file_uploaded=st.file_uploader("Upload your image here")
    if file_uploaded is not None:
        remove_button=st.button('Remove Background')
        if remove_button:
            with st.spinner('Removing Background from image'):
                image=file_uploaded.read()
                out_image=remove(image)

                col1,col2=st.columns(2)
                with col1:
                    st.image(image,caption='Origional Image',use_column_width=True)
                with col2:
                    st.image(out_image,caption='Background Removed Image',use_column_width=True)
                    st.download_button(label='Download',data=out_image,file_name='output.png')    
if __name__=='__main__':
    main()
