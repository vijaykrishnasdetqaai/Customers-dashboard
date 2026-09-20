import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io
from datetime import datetime

==========================================
EMBEDDED DATASET (100 Rows)
==========================================
csvdata = """UserID,FullName,EmailAddress,PhoneNumber,City,State,ProductCategory,ProductName,OrderDate,OrderAmountINR,PaymentMethod,DeliveryStatus
USR1001,Ravi Iyer,ravi.iyer26@email.com,+91 8181241943,Chennai,Tamil Nadu,Electronics,Smartphone 5G,2026-10-05 23:06,44647,Cash on Delivery,Delivered
USR1002,Aadhya Verma,aadhya.verma31@email.com,+91 7402418010,Chennai,Tamil Nadu,Electronics,Smartphone 5G,2026-10-17 19:01,37080,Credit Card,Shipped
USR1003,Lakshmi Desai,lakshmi.desai430@email.com,+91 7946785248,Pune,Maharashtra,Pooja Items,Premium Incense Sticks & Camphor Kit,2026-10-09 00:48,10762,Net Banking,Delivered
USR1004,Arjun Singh,arjun.singh981@email.com,+91 8445662585,Bengaluru,Karnataka,Traditional Wear,Men's Kurta Pajama Set,2026-10-13 03:22,22840,Cash on Delivery,Delivered
USR1005,Vivaan Gowda,vivaan.gowda550@email.com,+91 7536124280,Kolkata,West Bengal,Traditional Wear,Men's Kurta Pajama Set,2026-10-18 09:53,41497,Cash on Delivery,Pending
USR1006,Saanvi Mehta,saanvi.mehta197@email.com,+91 7298737106,Mysuru,Karnataka,Toys & Dolls,Traditional Wooden Golu Dolls Set,2026-10-08 09:05,15555,UPI,Delivered
USR1007,Pari Agarwal,pari.agarwal167@email.com,+91 8589915144,Delhi,Delhi,Electronics,Smartphone 5G,2026-10-22 08:44,45095,UPI,Shipped
USR1008,Sai Desai,sai.desai747@email.com,+91 8051454923,Hyderabad,Telangana,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-13 08:59,42242,Cash on Delivery,Delivered
USR1009,Diya Verma,diya.verma235@email.com,+91 7137869475,Delhi,Delhi,Sweets & Snacks,Premium Mysore Pak Box 1kg,2026-10-09 02:13,37469,Debit Card,Delivered
USR1010,Ananya Rao,ananya.rao906@email.com,+91 9761027762,Pune,Maharashtra,Electronics,Smart LED TV 43 inch,2026-10-09 04:15,49122,Cash on Delivery,Shipped
USR1011,Priya Mehta,priya.mehta439@email.com,+91 9506254832,Kolkata,West Bengal,Home Decor,Navaratri Golu Doll Stand,2026-10-08 04:32,32642,UPI,Shipped
USR1012,Meera Iyer,meera.iyer157@email.com,+91 9694860228,Hyderabad,Telangana,Toys & Dolls,Traditional Wooden Golu Dolls Set,2026-10-14 19:04,25515,Net Banking,Shipped
USR1013,Pari Joshi,pari.joshi258@email.com,+91 9376087131,Mysuru,Karnataka,Toys & Dolls,Traditional Wooden Golu Dolls Set,2026-10-24 03:43,35489,Debit Card,Shipped
USR1014,Diya Iyer,diya.iyer301@email.com,+91 8867302554,Hyderabad,Telangana,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-01 23:56,47463,Debit Card,Cancelled
USR1015,Rajesh Patel,rajesh.patel520@email.com,+91 7457031004,Coimbatore,Tamil Nadu,Home Decor,Brass Diya Set of 12,2026-10-21 16:38,13334,Credit Card,Delivered
USR1016,Sai Desai,sai.desai977@email.com,+91 9277851678,Mysuru,Karnataka,Pooja Items,Premium Incense Sticks & Camphor Kit,2026-10-11 15:01,7630,Debit Card,Pending
USR1017,Vikram Chatterjee,vikram.chatterjee246@email.com,+91 7248786714,Chennai,Tamil Nadu,Pooja Items,Premium Incense Sticks & Camphor Kit,2026-10-03 02:46,32148,UPI,Cancelled
USR1018,Riya Nair,riya.nair132@email.com,+91 9833608204,Pune,Maharashtra,Pooja Items,Eco-friendly Ganesha/Durga Idol,2026-10-06 08:33,40052,Net Banking,Cancelled
USR1019,Sunita Desai,sunita.desai774@email.com,+91 9962958940,Chennai,Tamil Nadu,Footwear,Women's Kolhapuri Chappals,2026-10-10 12:42,42889,Debit Card,Delivered
USR1020,Navya Gowda,navya.gowda124@email.com,+91 8064746525,Chennai,Tamil Nadu,Traditional Wear,Men's Kurta Pajama Set,2026-10-11 00:37,36600,Credit Card,Shipped
USR1021,Aarav Reddy,aarav.reddy725@email.com,+91 9710566582,Mysuru,Karnataka,Electronics,Smartphone 5G,2026-10-03 01:55,21953,UPI,Shipped
USR1022,Krishna Menon,krishna.menon220@email.com,+91 9315992115,Hyderabad,Telangana,Footwear,Women's Kolhapuri Chappals,2026-10-19 18:30,16224,Net Banking,Pending
USR1023,Reyansh Iyer,reyansh.iyer100@email.com,+91 9830309370,Kolkata,West Bengal,Home Decor,Navaratri Golu Doll Stand,2026-10-14 13:29,48079,UPI,Shipped
USR1024,Ravi Iyer,ravi.iyer63@email.com,+91 8729245242,Jaipur,Rajasthan,Home Decor,Navaratri Golu Doll Stand,2026-10-04 07:12,12764,Cash on Delivery,Delivered
USR1025,Aadhya Patel,aadhya.patel286@email.com,+91 8986972437,Chennai,Tamil Nadu,Traditional Wear,Men's Kurta Pajama Set,2026-10-15 17:06,3614,Cash on Delivery,Pending
USR1026,Aditya Kumar,aditya.kumar171@email.com,+91 8745535098,Pune,Maharashtra,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-07 12:57,4141,Credit Card,Delivered
USR1027,Anya Das,anya.das949@email.com,+91 8954246074,Mumbai,Maharashtra,Sweets & Snacks,Premium Mysore Pak Box 1kg,2026-10-23 23:50,36721,Net Banking,Delivered
USR1028,Ishaan Singh,ishaan.singh992@email.com,+91 7251183830,Vijayawada,Andhra Pradesh,Footwear,Women's Kolhapuri Chappals,2026-10-18 01:47,20851,UPI,Delivered
USR1029,Ananya Joshi,ananya.joshi942@email.com,+91 9281169403,Hyderabad,Telangana,Traditional Wear,Mysore Silk Saree,2026-10-17 02:54,12477,UPI,Shipped
USR1030,Suresh Kumar,suresh.kumar414@email.com,+91 7514909066,Vijayawada,Andhra Pradesh,Electronics,Smartphone 5G,2026-10-19 19:02,40890,UPI,Delivered
USR1031,Kavya Mehta,kavya.mehta536@email.com,+91 8358798143,Mumbai,Maharashtra,Electronics,Smartphone 5G,2026-10-22 22:20,15941,Debit Card,Delivered
USR1032,Suresh Chatterjee,suresh.chatterjee469@email.com,+91 8357970698,Bengaluru,Karnataka,Traditional Wear,Mysore Silk Saree,2026-10-15 19:36,6851,UPI,Shipped
USR1033,Navya Das,navya.das136@email.com,+91 8498981529,Bengaluru,Karnataka,Electronics,Smartphone 5G,2026-10-12 09:10,29015,Cash on Delivery,Shipped
USR1034,Siri Joshi,siri.joshi9@email.com,+91 9868450609,Ahmedabad,Gujarat,Home Decor,Brass Diya Set of 12,2026-10-22 03:56,9099,Debit Card,Delivered
USR1035,Vihaan Desai,vihaan.desai160@email.com,+91 8169726681,Mumbai,Maharashtra,Pooja Items,Premium Incense Sticks & Camphor Kit,2026-10-07 22:21,13641,Debit Card,Shipped
USR1036,Krishna Verma,krishna.verma95@email.com,+91 9724230947,Kolkata,West Bengal,Home Decor,Brass Diya Set of 12,2026-10-02 00:21,8872,Debit Card,Delivered
USR1037,Pari Desai,pari.desai723@email.com,+91 8836901321,Ahmedabad,Gujarat,Traditional Wear,Mysore Silk Saree,2026-10-04 02:56,45585,Credit Card,Shipped
USR1038,Vikram Agarwal,vikram.agarwal597@email.com,+91 9373077218,Hyderabad,Telangana,Sweets & Snacks,Premium Mysore Pak Box 1kg,2026-10-05 01:19,24196,UPI,Pending
USR1039,Reyansh Kumar,reyansh.kumar683@email.com,+91 7441495235,Delhi,Delhi,Pooja Items,Eco-friendly Ganesha/Durga Idol,2026-10-14 19:47,10427,Credit Card,Pending
USR1040,Kavita Patel,kavita.patel903@email.com,+91 8770791023,Mysuru,Karnataka,Electronics,Smart LED TV 43 inch,2026-10-24 10:50,27281,Credit Card,Delivered
USR1041,Kavita Iyer,kavita.iyer392@email.com,+91 7166320906,Pune,Maharashtra,Electronics,Smartphone 5G,2026-10-07 14:22,20299,Credit Card,Delivered
USR1042,Suresh Singh,suresh.singh409@email.com,+91 8409874348,Mumbai,Maharashtra,Traditional Wear,Men's Kurta Pajama Set,2026-10-25 08:22,42339,Cash on Delivery,Delivered
USR1043,Vikram Desai,vikram.desai340@email.com,+91 7118543408,Bengaluru,Karnataka,Home Decor,Brass Diya Set of 12,2026-10-06 18:16,2806,UPI,Shipped
USR1044,Saanvi Gupta,saanvi.gupta447@email.com,+91 9603647189,Ahmedabad,Gujarat,Traditional Wear,Men's Kurta Pajama Set,2026-10-13 18:12,16992,UPI,Shipped
USR1045,Aarav Joshi,aarav.joshi948@email.com,+91 9312633708,Coimbatore,Tamil Nadu,Footwear,Women's Kolhapuri Chappals,2026-10-24 23:42,13211,Debit Card,Delivered
USR1046,Suresh Gupta,suresh.gupta639@email.com,+91 8348257414,Coimbatore,Tamil Nadu,Traditional Wear,Men's Kurta Pajama Set,2026-10-24 09:32,20568,Net Banking,Delivered
USR1047,Lakshmi Chatterjee,lakshmi.chatterjee568@email.com,+91 7546696950,Chennai,Tamil Nadu,Sweets & Snacks,Premium Mysore Pak Box 1kg,2026-10-22 12:43,49328,Credit Card,Shipped
USR1048,Ishaan Rao,ishaan.rao562@email.com,+91 7001743499,Mumbai,Maharashtra,Home Decor,Brass Diya Set of 12,2026-10-07 13:50,38308,Cash on Delivery,Shipped
USR1049,Pari Gowda,pari.gowda453@email.com,+91 9901796894,Chennai,Tamil Nadu,Pooja Items,Eco-friendly Ganesha/Durga Idol,2026-10-16 23:10,43477,UPI,Delivered
USR1050,Suresh Bose,suresh.bose344@email.com,+91 7401094954,Chennai,Tamil Nadu,Toys & Dolls,Traditional Wooden Golu Dolls Set,2026-10-10 07:51,13349,Credit Card,Delivered
USR1051,Ayaan Menon,ayaan.menon626@email.com,+91 7312794864,Pune,Maharashtra,Sweets & Snacks,Premium Mysore Pak Box 1kg,2026-10-21 18:12,47376,Net Banking,Delivered
USR1052,Ayaan Nair,ayaan.nair672@email.com,+91 9953315788,Mysuru,Karnataka,Traditional Wear,Men's Kurta Pajama Set,2026-10-25 13:14,11825,Cash on Delivery,Delivered
USR1053,Riya Kumar,riya.kumar940@email.com,+91 7521231222,Pune,Maharashtra,Electronics,Smart LED TV 43 inch,2026-10-15 21:33,36928,Cash on Delivery,Delivered
USR1054,Rajesh Gowda,rajesh.gowda628@email.com,+91 9168005699,Kolkata,West Bengal,Pooja Items,Eco-friendly Ganesha/Durga Idol,2026-10-15 05:47,31407,Net Banking,Delivered
USR1055,Ayaan Das,ayaan.das785@email.com,+91 9238965651,Pune,Maharashtra,Toys & Dolls,Traditional Wooden Golu Dolls Set,2026-10-08 08:28,5376,Debit Card,Delivered
USR1056,Diya Gupta,diya.gupta915@email.com,+91 9319936135,Bengaluru,Karnataka,Electronics,Smart LED TV 43 inch,2026-10-05 07:24,45777,Credit Card,Shipped
USR1057,Aditya Hegde,aditya.hegde418@email.com,+91 8421124738,Ahmedabad,Gujarat,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-14 01:13,27833,Net Banking,Pending
USR1058,Kavya Sharma,kavya.sharma878@email.com,+91 9472571231,Kolkata,West Bengal,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-01 11:19,49678,Net Banking,Pending
USR1059,Vikram Hegde,vikram.hegde552@email.com,+91 9345620385,Vijayawada,Andhra Pradesh,Electronics,Smartphone 5G,2026-10-16 07:17,28861,Net Banking,Delivered
USR1060,Diya Rao,diya.rao742@email.com,+91 7708861714,Pune,Maharashtra,Electronics,Smart LED TV 43 inch,2026-10-20 17:01,26121,Cash on Delivery,Shipped
USR1061,Aarav Reddy,aarav.reddy659@email.com,+91 8840877826,Hyderabad,Telangana,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-06 01:16,25143,Debit Card,Delivered
USR1062,Diya Gupta,diya.gupta780@email.com,+91 8628334692,Mumbai,Maharashtra,Sweets & Snacks,Premium Mysore Pak Box 1kg,2026-10-09 02:30,1569,Cash on Delivery,Delivered
USR1063,Saanvi Kumar,saanvi.kumar666@email.com,+91 7294713656,Coimbatore,Tamil Nadu,Traditional Wear,Mysore Silk Saree,2026-10-25 00:15,13364,UPI,Shipped
USR1064,Ayaan Nair,ayaan.nair485@email.com,+91 9875303857,Bengaluru,Karnataka,Pooja Items,Premium Incense Sticks & Camphor Kit,2026-10-07 14:44,17092,Debit Card,Delivered
USR1065,Siri Iyer,siri.iyer797@email.com,+91 7703368777,Mumbai,Maharashtra,Traditional Wear,Men's Kurta Pajama Set,2026-10-19 00:59,20743,Cash on Delivery,Shipped
USR1066,Anya Rao,anya.rao965@email.com,+91 7851819913,Bengaluru,Karnataka,Pooja Items,Premium Incense Sticks & Camphor Kit,2026-10-23 20:15,6977,Debit Card,Pending
USR1067,Siri Iyer,siri.iyer816@email.com,+91 9430661792,Mysuru,Karnataka,Home Decor,Navaratri Golu Doll Stand,2026-10-18 13:42,24584,UPI,Shipped
USR1068,Diya Sharma,diya.sharma870@email.com,+91 8804138557,Pune,Maharashtra,Traditional Wear,Men's Kurta Pajama Set,2026-10-14 11:40,30428,Credit Card,Delivered
USR1069,Priya Joshi,priya.joshi989@email.com,+91 9793693337,Mumbai,Maharashtra,Pooja Items,Premium Incense Sticks & Camphor Kit,2026-10-18 15:29,28844,Cash on Delivery,Delivered
USR1070,Meera Kumar,meera.kumar851@email.com,+91 7372214308,Mumbai,Maharashtra,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-08 14:36,40297,Net Banking,Delivered
USR1071,Ananya Gupta,ananya.gupta187@email.com,+91 9094011037,Chennai,Tamil Nadu,Home Decor,Navaratri Golu Doll Stand,2026-10-09 10:17,39368,Debit Card,Shipped
USR1072,Navya Singh,navya.singh88@email.com,+91 8036616336,Jaipur,Rajasthan,Sweets & Snacks,Premium Mysore Pak Box 1kg,2026-10-16 17:48,16048,Net Banking,Shipped
USR1073,Ananya Gowda,ananya.gowda812@email.com,+91 7074059253,Bengaluru,Karnataka,Home Decor,Brass Diya Set of 12,2026-10-08 12:44,16244,Debit Card,Shipped
USR1074,Saanvi Menon,saanvi.menon567@email.com,+91 9280292341,Delhi,Delhi,Sweets & Snacks,Premium Mysore Pak Box 1kg,2026-10-24 17:21,23355,Net Banking,Delivered
USR1075,Krishna Kumar,krishna.kumar124@email.com,+91 7827143233,Delhi,Delhi,Traditional Wear,Men's Kurta Pajama Set,2026-10-24 17:48,45529,Credit Card,Delivered
USR1076,Priya Menon,priya.menon284@email.com,+91 9532256470,Ahmedabad,Gujarat,Pooja Items,Premium Incense Sticks & Camphor Kit,2026-10-10 03:53,13020,Debit Card,Delivered
USR1077,Sai Chatterjee,sai.chatterjee15@email.com,+91 9294092753,Hyderabad,Telangana,Home Decor,Brass Diya Set of 12,2026-10-02 01:35,19444,Credit Card,Shipped
USR1078,Rajesh Menon,rajesh.menon106@email.com,+91 7052679490,Vijayawada,Andhra Pradesh,Home Decor,Brass Diya Set of 12,2026-10-16 15:28,22627,Credit Card,Cancelled
USR1079,Krishna Menon,krishna.menon117@email.com,+91 7280647907,Kolkata,West Bengal,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-03 18:40,45286,UPI,Delivered
USR1080,Kavita Mehta,kavita.mehta972@email.com,+91 8304963614,Bengaluru,Karnataka,Electronics,Smartphone 5G,2026-10-04 17:48,27573,Cash on Delivery,Shipped
USR1081,Siri Kumar,siri.kumar795@email.com,+91 9244431947,Kolkata,West Bengal,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-15 09:55,38868,Net Banking,Delivered
USR1082,Siri Verma,siri.verma625@email.com,+91 7426204934,Chennai,Tamil Nadu,Toys & Dolls,Traditional Wooden Golu Dolls Set,2026-10-07 08:42,5619,Credit Card,Delivered
USR1083,Riya Reddy,riya.reddy161@email.com,+91 7011492154,Kolkata,West Bengal,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-23 19:30,19386,UPI,Delivered
USR1084,Lakshmi Chatterjee,lakshmi.chatterjee720@email.com,+91 8950049698,Bengaluru,Karnataka,Toys & Dolls,Traditional Wooden Golu Dolls Set,2026-10-08 08:50,41262,Cash on Delivery,Shipped
USR1085,Sunita Singh,sunita.singh436@email.com,+91 7492960451,Ahmedabad,Gujarat,Electronics,Smartphone 5G,2026-10-21 04:58,17707,Credit Card,Delivered
USR1086,Sai Chatterjee,sai.chatterjee610@email.com,+91 9444725646,Mumbai,Maharashtra,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-04 14:44,20227,Net Banking,Pending
USR1087,Navya Desai,navya.desai506@email.com,+91 8880160025,Bengaluru,Karnataka,Pooja Items,Premium Incense Sticks & Camphor Kit,2026-10-02 13:47,21422,Cash on Delivery,Delivered
USR1088,Aditya Kumar,aditya.kumar985@email.com,+91 9896089430,Vijayawada,Andhra Pradesh,Pooja Items,Premium Incense Sticks & Camphor Kit,2026-10-01 21:52,17961,Cash on Delivery,Delivered
USR1089,Rajesh Patel,rajesh.patel482@email.com,+91 9228932714,Coimbatore,Tamil Nadu,Sweets & Snacks,Assorted Indian Mithai Box,2026-10-09 05:37,28865,Net Banking,Cancelled
USR1090,Ananya Agarwal,ananya.agarwal419@email.com,+91 8431548670,Delhi,Delhi,Toys & Dolls,Traditional Wooden Golu Dolls Set,2026-10-04 05:21,27276,Net Banking,Delivered
USR1091,Anya Desai,anya.desai38@email.com,+91 8953462417,Bengaluru,Karnataka,Home Decor,Navaratri Golu Doll Stand,2026-10-09 10:07,26787,Cash on Delivery,Pending
USR1092,Aarav Desai,aarav.desai474@email.com,+91 8774884818,Mysuru,Karnataka,Electronics,Smartphone 5G,2026-10-17 11:39,49873,Net Banking,Shipped
USR1093,Rajesh Verma,rajesh.verma209@email.com,+91 8146997816,Ahmedabad,Gujarat,Electronics,Smart LED TV 43 inch,2026-10-10 14:56,46059,Net Banking,Delivered
USR1094,Ravi Bose,ravi.bose819@email.com,+91 8027774780,Jaipur,Rajasthan,Electronics,Smart LED TV 43 inch,2026-10-10 17:00,36491,Net Banking,Delivered
USR1095,Vikram Iyer,vikram.iyer473@email.com,+91 7504513251,Coimbatore,Tamil Nadu,Electronics,Smart LED TV 43 inch,2026-10-16 22:18,33648,Debit Card,Delivered
USR1096,Ananya Menon,ananya.menon250@email.com,+91 8961882949,Ahmedabad,Gujarat,Electronics,Smart LED TV 43 inch,2026-10-13 06:58,39579,Cash on Delivery,Shipped
USR1097,Arjun Reddy,arjun.reddy283@email.com,+91 8782164134,Delhi,Delhi,Pooja Items,Eco-friendly Ganesha/Durga Idol,2026-10-09 00:18,47881,Debit Card,Pending
USR1098,Kavya Menon,kavya.menon887@email.com,+91 7638212450,Pune,Maharashtra,Pooja Items,Eco-friendly Ganesha/Durga Idol,2026-10-16 11:21,36469,Cash on Delivery,Delivered
USR1099,Sunita Gupta,sunita.gupta891@email.com,+91 7810255760,Jaipur,Rajasthan,Electronics,Smartphone 5G,2026-10-19 12:14,27219,UPI,Delivered
USR1100,Ananya Rao,ananya.rao396@email.com,+91 9850521812,Coimbatore,Tamil Nadu,Electronics,Smart LED TV 43 inch,2026-10-16 01:08,33217,Cash on Delivery,Delivered"""

==========================================
DATA LOADING & PREPROCESSING
==========================================
@st.cache_data
def load_data():
    df = pd.readcsv(io.StringIO(csvdata))
    df['OrderDate'] = pd.todatetime(df['Order_Date'])
    return df

df = load_data()

==========================================
STREAMLIT PAGE CONFIG & FUTURISTIC THEME
==========================================
st.setpageconfig(
    page_title="Dasara 2026 Analytics Hub",
    page_icon="🪔",
    layout="wide",
    initialsidebarstate="expanded"
)

Futuristic Dark Theme with Neon Accents
st.markdown("""

/ Import Modern Fonts /
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/ Global Background - Dark Gradient /
.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1419 100%);
    color: #e4e6eb;
}

/ Main Container /
.main .block-container {
    padding: 2rem 3rem;
    max-width: 1600px;
}

/ Header Styling /
.main-header {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #00d4ff 0%, #ff006e 50%, #ffd700 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin-bottom: 0.5rem;
    letter-spacing: -1px;
    text-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
}

.sub-header {
    font-family: 'Inter', sans-serif;
    font-size: 1.1rem;
    color: #8b92a8;
    text-align: center;
    margin-bottom: 3rem;
    font-weight: 300;
    letter-spacing: 0.5px;
}

/ Glassmorphism Cards /
.glass-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
}

.glass-card:hover {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.15);
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(0, 212, 255, 0.15);
}

/ KPI Metric Cards /
.stMetric {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.08) 0%, rgba(255, 0, 110, 0.08) 100%);
    border: 1px solid rgba(0, 212, 255, 0.2);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 20px rgba(0, 212, 255, 0.1);
    transition: all 0.3s ease;
}

.stMetric:hover {
    border: 1px solid rgba(0, 212, 255, 0.4);
    box-shadow: 0 6px 30px rgba(0, 212, 255, 0.2);
}

.stMetric label {
    color: #8b92a8 !important;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stMetric .metric-value {
    color: #00d4ff !important;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2rem;
    font-weight: 700;
}

/ Sidebar /
.css-1d391kg {
    background: rgba(10, 14, 39, 0.95);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.css-1d391kg .stSelectbox label,
.css-1d391kg .stDateInput label,
.css-1d391kg .stMultiselect label {
    color: #00d4ff !important;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-size: 0.85rem;
}

/ Section Headers /
.section-header {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 600;
    color: #00d4ff;
    margin-top: 2rem;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(0, 212, 255, 0.2);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/ Chart Containers /
.stPlotlyChart {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 1rem;
    margin: 1rem 0;
}

/ Status Badges /
.status-badge {
    display: inline-block;
    padding: 0.4rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.status-delivered {
    background: rgba(40, 180, 99, 0.2);
    color: #28b463;
    border: 1px solid rgba(40, 180, 99, 0.3);
}

.status-shipped {
    background: rgba(46, 134, 193, 0.2);
    color: #2e86c1;
    border: 1px solid rgba(46, 134, 193, 0.3);
}

.status-pending {
    background: rgba(255, 153, 51, 0.2);
    color: #ff9933;
    border: 1px solid rgba(255, 153, 51, 0.3);
}

.status-cancelled {
    background: rgba(196, 30, 58, 0.2);
    color: #c41e3a;
    border: 1px solid rgba(196, 30, 58, 0.3);
}

/ Tabs /
.stTabs [data-baseweb="tab-list"] {
    gap: 2rem;
    background: rgba(255, 255, 255, 0.02);
    padding: 0.5rem;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.stTabs [data-baseweb="tab"] {
    color: #8b92a8;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 0.95rem;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.15) 0%, rgba(255, 0, 110, 0.15) 100%);
    color: #00d4ff;
    border: 1px solid rgba(0, 212, 255, 0.3);
}

/ Expander /
.streamlit-expanderHeader {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    color: #00d4ff !important;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
}

/ Dataframe /
.dataframe {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
}

/ Scrollbar /
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #00d4ff 0%, #ff006e 100%);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #00b8d9 0%, #e6005c 100%);
}

/ Animations /
@keyframes glow {
    0%, 100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.3); }
    50% { box-shadow: 0 0 30px rgba(0, 212, 255, 0.5); }
}

.glow-effect {
    animation: glow 3s ease-in-out infinite;
}

/ Divider /
.stDivider {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    margin: 2rem 0;
}

""", unsafeallowhtml=True)

Header
st.markdown('🪔 Dasara 2026 Analytics Hub', unsafeallowhtml=True)
st.markdown('Real-time insights for Traditional Wear, Pooja Items, Electronics & More', unsafeallowhtml=True)

==========================================
SIDEBAR FILTERS
==========================================
st.sidebar.markdown("## 🔍 Filter Controls")
st.sidebar.markdown("---")

Date Range Filter
mindate = df['OrderDate'].min().date()
maxdate = df['OrderDate'].max().date()
selecteddates = st.sidebar.dateinput(
    "📅 Order Date Range",
    [mindate, maxdate],
    minvalue=mindate,
    maxvalue=maxdate
)

Categorical Filters
st.sidebar.markdown("### 📍 Location")
states = st.sidebar.multiselect(
    "State",
    options=sorted(df['State'].unique()),
    default=sorted(df['State'].unique())
)

st.sidebar.markdown("### 🛍️ Products")
categories = st.sidebar.multiselect(
    "Product Category",
    options=sorted(df['Product_Category'].unique()),
    default=sorted(df['Product_Category'].unique())
)

st.sidebar.markdown("### 💳 Payment")
payment_methods = st.sidebar.multiselect(
    "Payment Method",
    options=sorted(df['Payment_Method'].unique()),
    default=sorted(df['Payment_Method'].unique())
)

st.sidebar.markdown("### 🚚 Delivery")
delivery_status = st.sidebar.multiselect(
    "Delivery Status",
    options=sorted(df['Delivery_Status'].unique()),
    default=sorted(df['Delivery_Status'].unique())
)

Apply Filters
filtered_df = df[
    (df['OrderDate'].dt.date >= selecteddates[0]) &
    (df['OrderDate'].dt.date  0 else 0
deliveredcount = len(filtereddf[filtereddf['DeliveryStatus'] == 'Delivered'])
deliveryrate = (deliveredcount / totalorders * 100) if totalorders > 0 else 0

st.markdown("### 📊 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    
        💰
        Total Revenue
        ₹{total_revenue:,.0f}
    
    """, unsafeallowhtml=True)

with col2:
    st.markdown(f"""
    
        📦
        Total Orders
        {total_orders:,}
    
    """, unsafeallowhtml=True)

with col3:
    st.markdown(f"""
    
        📊
        Avg Order Value
        ₹{aov:,.0f}
    
    """, unsafeallowhtml=True)

with col4:
    st.markdown(f"""
    
        ✅
        Delivery Success
        {delivery_rate:.1f}%
    
    """, unsafeallowhtml=True)

st.markdown("---")

==========================================
TABBED VISUALIZATIONS
==========================================
tab1, tab2, tab3 = st.tabs(["📈 Sales Analytics", "🗺️ Geographic Insights", "🛍️ Product Performance"])

Festive Color Palette
festive_colors = ["#00d4ff", "#ff006e", "#ffd700", "#2e86c1", "#28b463", "#8e44ad"]

with tab1:
    st.markdown("### 📈 Sales Trends & Patterns")
    
    colchart1, colchart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("#### Daily Revenue Trend")
        dailysales = filtereddf.groupby(filtereddf['OrderDate'].dt.date)['OrderAmountINR'].sum().reset_index()
        daily_sales.columns = ['Date', 'Revenue']
        
        fig_trend = go.Figure()
        figtrend.addtrace(go.Scatter(
            x=daily_sales['Date'],
            y=daily_sales['Revenue'],
            mode='lines+markers',
            line=dict(color='#00d4ff', width=3),
            marker=dict(size=8, color='#ff006e', line=dict(width=2, color='#00d4ff')),
            fill='tozeroy',
            fillcolor='rgba(0, 212, 255, 0.1)'
        ))
        
        figtrend.updatelayout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e4e6eb', family='Inter'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.05)', title='Date'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.05)', title='Revenue (₹)'),
            hovermode='x unified',
            height=400
        )
        st.plotlychart(figtrend, usecontainerwidth=True)
    
    with col_chart2:
        st.markdown("#### Revenue by State")
        statesales = filtereddf.groupby('State')['OrderAmountINR'].sum().resetindex().sortvalues(by='OrderAmountINR', ascending=True)
        
        fig_state = go.Figure()
        figstate.addtrace(go.Bar(
            x=statesales['OrderAmount_INR'],
            y=state_sales['State'],
            orientation='h',
            marker=dict(
                color=statesales['OrderAmount_INR'],
                colorscale='Viridis',
                showscale=False
            )
        ))
        
        figstate.updatelayout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e4e6eb', family='Inter'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.05)', title='Revenue (₹)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
            height=400
        )
        st.plotlychart(figstate, usecontainerwidth=True)

with tab2:
    st.markdown("### 🗺️ Geographic Distribution")
    
    colchart3, colchart4 = st.columns(2)
    
    with col_chart3:
        st.markdown("#### Orders by State")
        stateorders = filtereddf.groupby('State').size().reset_index(name='Orders')
        stateorders = stateorders.sort_values('Orders', ascending=False)
        
        figstateorders = go.Figure(data=[go.Pie(
            labels=state_orders['State'],
            values=state_orders['Orders'],
            hole=0.4,
            marker=dict(colors=festive_colors),
            textinfo='label+percent',
            textposition='inside'
        )])
        
        figstateorders.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e4e6eb', family='Inter'),
            height=400
        )
        st.plotlychart(figstateorders, usecontainer_width=True)
    
    with col_chart4:
        st.markdown("#### Top Cities by Revenue")
        citysales = filtereddf.groupby('City')['OrderAmountINR'].sum().reset_index()
        citysales = citysales.sortvalues('OrderAmount_INR', ascending=True).tail(10)
        
        fig_city = go.Figure()
        figcity.addtrace(go.Bar(
            x=citysales['OrderAmount_INR'],
            y=city_sales['City'],
            orientation='h',
            marker=dict(
                color=citysales['OrderAmount_INR'],
                colorscale='Plasma',
                showscale=False
            )
        ))
        
        figcity.updatelayout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e4e6eb', family='Inter'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.05)', title='Revenue (₹)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
            height=400
        )
        st.plotlychart(figcity, usecontainerwidth=True)

with tab3:
    st.markdown("### 🛍️ Product & Category Analysis")
    
    colchart5, colchart6 = st.columns(2)
    
    with col_chart5:
        st.markdown("#### Revenue by Category")
        catsales = filtereddf.groupby('ProductCategory')['OrderAmountINR'].sum().resetindex()
        
        fig_cat = go.Figure(data=[go.Pie(
            labels=catsales['ProductCategory'],
            values=catsales['OrderAmount_INR'],
            hole=0.5,
            marker=dict(colors=festive_colors),
            textinfo='label+percent+value',
            textposition='inside',
            textfont=dict(size=12)
        )])
        
        figcat.updatelayout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e4e6eb', family='Inter'),
            height=400
        )
        st.plotlychart(figcat, usecontainerwidth=True)
    
    with col_chart6:
        st.markdown("#### Top 5 Products")
        productsales = filtereddf.groupby('ProductName')['OrderAmountINR'].sum().resetindex()
        productsales = productsales.sortvalues('OrderAmount_INR', ascending=True).tail(5)
        
        fig_prod = go.Figure()
        figprod.addtrace(go.Bar(
            x=productsales['OrderAmount_INR'],
            y=productsales['ProductName'],
            orientation='h',
            marker=dict(
                color=['#00d4ff', '#ff006e', '#ffd700', '#28b463', '#8e44ad'],
                showscale=False
            )
        ))
        
        figprod.updatelayout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e4e6eb', family='Inter'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.05)', title='Revenue (₹)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
            height=400
        )
        st.plotlychart(figprod, usecontainerwidth=True)

st.markdown("---")

==========================================
PAYMENT & DELIVERY ANALYSIS
==========================================
st.markdown("### 💳 Payment & Delivery Insights")

colchart7, colchart8 = st.columns(2)

with col_chart7:
    st.markdown("#### Payment Method Distribution")
    paymentcounts = filtereddf['PaymentMethod'].valuecounts().reset_index()
    payment_counts.columns = ['Payment Method', 'Count']
    
    fig_pay = go.Figure(data=[go.Pie(
        labels=payment_counts['Payment Method'],
        values=payment_counts['Count'],
        hole=0.5,
        marker=dict(colors=festive_colors),
        textinfo='label+percent',
        textposition='inside'
    )])
    
    figpay.updatelayout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e4e6eb', family='Inter'),
        height=350
    )
    st.plotlychart(figpay, usecontainerwidth=True)

with col_chart8:
    st.markdown("#### Delivery Status Breakdown")
    statuscounts = filtereddf['DeliveryStatus'].valuecounts().reset_index()
    status_counts.columns = ['Status', 'Count']
    
    status_colors = {
        'Delivered': '#28b463',
        'Shipped': '#2e86c1',
        'Pending': '#ff9933',
        'Cancelled': '#c41e3a'
    }
    
    fig_status = go.Figure(data=[go.Pie(
        labels=status_counts['Status'],
        values=status_counts['Count'],
        hole=0.5,
        marker=dict(colors=[statuscolors.get(s, '#8b92a8') for s in statuscounts['Status']]),
        textinfo='label+percent',
        textposition='inside'
    )])
    
    figstatus.updatelayout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e4e6eb', family='Inter'),
        height=350
    )
    st.plotlychart(figstatus, usecontainerwidth=True)

st.markdown("---")

==========================================
RAW DATA EXPANDER
==========================================
with st.expander("📋 View Complete Dataset", expanded=False):
    st.dataframe(
        filtered_df[[
            'UserID', 'FullName', 'City', 'State', 
            'ProductCategory', 'ProductName', 'Order_Date', 
            'OrderAmountINR', 'PaymentMethod', 'DeliveryStatus'
        ]],
        usecontainerwidth=True,
        height=400
    )

Footer
st.markdown("---")
st.markdown("""

    🪔 Dasara 2026 E-commerce Analytics Dashboard
    Powered by Streamlit & Plotly | Built with ❤️ for festive commerce insights

""", unsafeallowhtml=True)

🎨 Key UI/UX Improvements:

Futuristic Dark Theme
Deep gradient background (navy to dark blue)
Glassmorphism cards with backdrop blur
Neon accent colors (cyan, magenta, gold)

Modern Typography
Space Grotesk for headers (futuristic, geometric)
Inter for body text (clean, readable)
Proper hierarchy with letter-spacing

Enhanced Visual Elements
Animated glow effects on hover
Gradient text for main header
Status badges with color coding
Custom scrollbars with gradients

Better Organization
Tabbed interface for logical grouping
Sectioned sidebar filters
Clear visual hierarchy
Proper spacing and breathing room

Advanced Charts
Custom Plotly themes matching the UI
Gradient fills and markers
Better hover interactions
Consistent color palette

Professional Polish
Glassmorphism KPI cards with icons
Smooth transitions and animations
Professional footer
Responsive layout

The dashboard now looks like a premium SaaS analytics platform with a futuristic, cyberpunk-inspired aesthetic perfect for showcasing festive e-commerce data! 🚀
