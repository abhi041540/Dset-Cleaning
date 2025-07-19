import io
import streamlit as st
import pandas as pd
import datacleaning as dc
import time
st.set_page_config(page_title="Dset Cheaning",page_icon="logo.png",layout="wide")
st.markdown("""
<style>
.st-emotion-cache-ajtf3x 
{
display:block;
}
.elbt1zu4
{
padding:0px 5px;
}
#dset-cleaning
{
padding:0px;
margin-left:10px;
margin-top:10px;
color: rgb(239 106 7);
font-size:250%;
width:100vw;
}
#make-the-dataset-clean-in-one-click
{
text-align:center;
}
#stBaseButton-secondary
{
visibility:"hidden";
}
.e16xj5sw0
{
height:500px;
margin:10px;
margin-bottom:10px;
display:flex;
align-items:center;
justify-content:center;
margin-top: 20px;
}
.e16xj5sw1
{
margin-right:0;
display:block;
}
.e16xj5sw2
{
    width: 100%;
    margin-right: 1rem;
    text-align: center;
    display: block;
    color:black;
}
.st-emotion-cache-bfgnao,.st-emotion-cache-1weic72
{
    color: rgb(239 106 7);
    margin:0 auto;
    font-family: serif;
    font-weight: 600;
    font-size: 150%;
    width:160px;
}
.e16xj5sw5
{
background-color: orange;
margin-bottom: 20px;
}
.stToastContainer
{
display:flex;
align-items:center;
justify-content:center;
}
.stAlertContainer
{
text-align:center;
}
.st-emotion-cache-1gulkj5 .st-emotion-cache-1rwb540,.st-emotion-cache-1erivf3 .st-emotion-cache-z8vbw2
{
position:absolute;
visibility:hidden;
}
.stDownloadButton .st-emotion-cache-1rwb540,.stDownloadButton .st-emotion-cache-z8vbw2 
{
width:100vw;
margin-bottom:20px;
}
.st-emotion-cache-1an99fx,.st-emotion-cache-1o77jex
{
    margin: 2% 3%;
    background-color: gainsboro;
    padding: 15px;
    font-size: 120%;
    font-weight: 600;
    border-radius: 5px;
    
}
.st-emotion-cache-1o77jex
{
color:black;
}
.footer
{
    padding: 20px;
    font-family: serif;
    font-size: 120%;
    background: antiquewhite;
    margin-bottom: 10px;
    color:black;
}
.st-emotion-cache-1ort0lt
{
    width: 100%;
    text-align: center;
}
.st-emotion-cache-u8hs99
{
    width: 100%;
    text-align: center;
}
</style>""",unsafe_allow_html=True)

col1=st.columns(4)
with col1[0]:
  st.header("Dset-Cleaning")
st.title("Make The Dataset Clean In One Click")
st.info("The last column is assumed to represent the output feature for model training!")
st.file_uploader(label="upload dataset file",type=["csv"],key="file")
# print(st.session_state)
df=None
if st.session_state["file"] !=None:
  st.toast("🎉 File uploaded successfully!", icon="📁")
  ds_file=None
  m=0
  with st.spinner("Processing your file..."):
    df = st.session_state['file']
    dataset = pd.read_csv(df)
    data1=dc.dataClaning(dataset)
    file1=io.StringIO()
    data1.to_csv(file1,index=False)
    ds_file=file1.getvalue()
    m=1
    time.sleep(5)  # simulate some processing
    st.success("✅ Done!")

  if m==1 :
    st.download_button(
      label="📁 Download CSV",
      data=ds_file,
      file_name=st.session_state["file"].name if "_Dset-Cleaning" in st.session_state["file"].name else st.session_state["file"].name.replace(".csv", "_Dset-Cleaning.csv") ,
      mime="text/csv"
    )

st.markdown("""
<style>
.st-emotion-cache-xhkv9f
{
  margin: 1% 4%;
  border: 1px solid gray;
  border-radius: 10px;
  # box-shadow: 10px 10px 10px gray;
  padding: 8px;
  background-color: rgb(255 127 21);
  box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
}
</style>""",unsafe_allow_html=True)
st.image("ds_image.png",use_container_width=True)
content="""🧼 Dset Cheaning — The Ultimate Dataset Cleanup Companion Say goodbye to messy data and hello to smooth preprocessing. Dset Cheaning is a robust, intuitive platform crafted for data analysts, ML engineers, and curious coders who need clean, reliable datasets without the usual hassle.

🔍 Whether you're tackling thousands of rows or just a small sample, Dset Cheaning helps you:

🚫 Eliminate duplicate entries for lean, meaningful data

📉 Detect and remove outliers to preserve statistical integrity

⚠️ Handle missing values with intelligent imputation and minimal data loss

🎯 Ensure consistency across your dataset for streamlined analysis

With powerful tools and a clean interface, Dset Cheaning makes data preparation feel less like a chore and more like progress. Your insights deserve clean input....\nlet us help you get there."""
st.text(content)

st.markdown(f"""<div class="footer">© {time.strftime('%Y')} Dset Cheaning. All rights reserved.</div>""",unsafe_allow_html=True)



