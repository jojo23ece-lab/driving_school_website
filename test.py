import streamlit as st
from streamlit_option_menu import option_menu
import calendar
from datetime import datetime

st.set_page_config(page_title='SRINIVASA MOTOR DRIVING SCHOOL',page_icon='😄', layout='wide')
st.image(r"C:\Users\NITHYANANDAN EDWARD\OneDrive\Attachments\Pictures\Screenshots\Screenshot 2025-09-09 134430.png", width=400)

# Initialize events in session state
if 'events' not in st.session_state:
    st.session_state.events = {
        5: "Beginner Training - 10 AM",
        10: "Mock Test - 2 PM",
        15: "Advanced Course - 9 AM",
        20: "Safety Workshop - 11 AM"
    }

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['about','location','course','calendar','blog'],  # Added 'calendar'
    )

if selected=='about':
    st.title('SRINIVASA MOTOR DRIVING SCHOOL')
    st.image(r"C:\Users\NITHYANANDAN EDWARD\Screenshot 2025-10-28 105405.png")
    st.header('Srinivas Reddy Building, Marathahalli Main Rd,/n near Old Bus Stop, above Srinivasa MRP, HAL Central Township, Marathahalli Village,/n Marathahalli, Bengaluru, Karnataka 560037')
    st.subheader('WHY CHOOSE US!🤝')
    st.write("SRINIVASA MOTOR DRIVING SCHOOL, our driving school is a well established center which provides our learners with the right training facilitructors are licensed professionals, and also exprienced drivers. our driving instructors are well mannered and discplined experts")
    st.write(' 👉our driving instructors are licensed professionals')
    st.write('👉and also exprienced drivers.')
    st.write(' 👉our driving instructors are well mannered and discplined experts')
    st.write('09481482060')
    st.write('\nMonday 6 am–8 pm')
    st.write('Tuesday 6 am–8 pm')
    st.write('Wednesday 6 am–8 pm')
    st.write('Thursday 6 am–8 pm')
    st.write('Friday 6 am–8 pm')
    st.write('Sunday Closed')

if selected=='location':
    st.title('SRINIVASA MOTOR DRIVING SCHOOL')
    st.image(r"C:\Users\NITHYANANDAN EDWARD\Screenshot 2025-10-28 101851.png",width=200)
    st.image(r"C:\Users\NITHYANANDAN EDWARD\Screenshot 2025-10-28 102213.png",width=200)
    st.header('located at srinivasa reddy building,marathahalli market')
    st.markdown('[🗺️ View on Google Maps]marathahalli bangalore: 560037 https://www.google.com/maps/place/Srinivasa+Motor+Driving+Training+School/@12.9555169,77.6919121,17z/data=!3m1!4b1!4m6!3m5!1s0x3bae13ceb881462d:0xda06fc705063ddb3!8m2!3d12.9555169!4d77.6919121!16s%2Fg%2F1v1tljcz?entry=ttu&g_ep=EgoyMDI1MDkwMy4wIKXMDSoASAFQAw%3D%3D')

if selected=='course':
    st.header("Course Registration")
    st.markdown("### Would you like to join our driving school?")
    
    status = st.radio("Choose an option:", ['Sure', 'No'])
    
    if status == 'Sure':
        st.success("Welcome to our driving school! 🎉")
        
        st.write("---")
        st.subheader("Course Details")
        
        vehicle_type = st.selectbox('Type of Vehicle:', ['Geared', 'Automatic'])
        st.info(f"Selected: {vehicle_type}")
        
        vehicle_pref = st.selectbox('Preference of Vehicle:', ['Personal', 'Institute Vehicle'])
        st.info(f"Selected: {vehicle_pref}")
        
        if st.button("Submit Registration", type="primary"):
            st.balloons()
            st.success(f"""
            ✅ Thank you for registering!
            
            **Your Selections:**
            - Vehicle Type: {vehicle_type}
            - Vehicle Preference: {vehicle_pref}
            
            We'll contact you soon!
            """)
    else:
        st.write('thank you for visiting,feel free to comeback anytime')

# ================================
# NEW CALENDAR SECTION
# ================================
if selected == 'calendar':
    st.title('📅 Training Schedule Calendar')
    
    # Two columns: Calendar view and Edit section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Month and Year selector
        year = st.number_input("Year:", min_value=2024, max_value=2030, value=2025)
        month = st.selectbox("Month:", range(1, 13), index=10, 
                           format_func=lambda x: calendar.month_name[x])
        
        # Create calendar
        cal = calendar.monthcalendar(year, month)
        
        st.write(f"### {calendar.month_name[month]} {year}")
        
        # Header
        cols = st.columns(7)
        for i, day in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
            cols[i].markdown(f"**{day}**")
        
        # Calendar grid
        for week in cal:
            cols = st.columns(7)
            for i, day in enumerate(week):
                if day == 0:
                    cols[i].write("")
                else:
                    # Check if day has event
                    if day in st.session_state.events:
                        cols[i].markdown(f"**:red[{day}]**")
                        cols[i].caption(f"📌 {st.session_state.events[day]}")
                    else:
                        cols[i].write(str(day))
    
    with col2:
        st.write("### ✏️ Manage Events")
        
        # Add new event
        st.write("**Add Event:**")
        new_day = st.number_input("Day:", min_value=1, max_value=31, value=1, key="new_day")
        new_event = st.text_input("Event:", placeholder="e.g., Training - 10 AM", key="new_event")
        
        if st.button("➕ Add Event"):
            if new_event:
                st.session_state.events[new_day] = new_event
                st.success(f"✅ Event added on day {new_day}!")
                st.rerun()
            else:
                st.error("Please enter an event name!")
        
        st.write("---")
        
        # Delete event
        st.write("**Delete Event:**")
        if st.session_state.events:
            day_to_delete = st.selectbox("Select day:", list(st.session_state.events.keys()))
            st.write(f"Event: {st.session_state.events[day_to_delete]}")
            
            if st.button("🗑️ Delete Event"):
                del st.session_state.events[day_to_delete]
                st.success("Event deleted!")
                st.rerun()
        else:
            st.info("No events to delete")
        
        st.write("---")
        
        # Show all events
        st.write("**All Events:**")
        if st.session_state.events:
            for day, event in sorted(st.session_state.events.items()):
                st.write(f"📅 Day {day}: {event}")
        else:
            st.info("No events scheduled")

if selected== 'blog':
    name=st.text_input('comments')
    st.write(name)
    rate=st.slider('rate us',min_value=1,max_value=5)
    st.write(rate)
    for i in range(rate):
        st.write('⭐')

tab1,tab2,tab3=st.tabs(['about','location','mock test'])
with tab1:
    st.write("SRINIVASA MOTOR DRIVING SCHOOL, our driving school is a well established center which provides our learners with the right training facilitructors are licensed professionals, and also exprienced drivers. our driving instructors are well mannered and discplined experts")
    st.write('our driving instructors are licensed professionals, and also exprienced drivers. our driving instructors are well mannered and discplined experts')
with tab2:
    st.header('located at srinivasa reddy building,marathahalli market')
    st.markdown('[🗺️ View on Google Maps]marathahalli bangalore: 560037 https://www.google.com/maps/place/Srinivasa+Motor+Driving+Training+School/@12.9555169,77.6919121,17z/data=!3m1!4b1!4m6!3m5!1s0x3bae13ceb881462d:0xda06fc705063ddb3!8m2!3d12.9555169!4d77.6919121!16s%2Fg%2F1v1tljcz?entry=ttu&g_ep=EgoyMDI1MDkwMy4wIKXMDSoASAFQAw%3D%3D')
with tab3:
    video_file = open(r"C:\Users\NITHYANANDAN EDWARD\Downloads\videoplayback.mp4", 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)