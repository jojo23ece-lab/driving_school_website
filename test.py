import streamlit as st
from streamlit_option_menu import option_menu
import calendar
from datetime import datetime

st.set_page_config(page_title='SRINIVASA MOTOR DRIVING SCHOOL',page_icon='😄', layout='wide')

# ✅ FIXED: Use relative path
st.image("logo.png", width=400)

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
        options=['about','location','course','calendar','blog','mock test'],
    )

if selected=='about':
    st.title('SRINIVASA MOTOR DRIVING SCHOOL')
    # ✅ FIXED: Use relative path
    st.image("school.png")
    st.header('Srinivas Reddy Building, Marathahalli Main Rd, near Old Bus Stop, above Srinivasa MRP, HAL Central Township, Marathahalli Village, Marathahalli, Bengaluru, Karnataka 560037')
    st.subheader('WHY CHOOSE US!🤝')
    st.write("SRINIVASA MOTOR DRIVING SCHOOL, our driving school is a well established center which provides our learners with the right training facilities. Our driving instructors are licensed professionals, and also experienced drivers. Our driving instructors are well mannered and disciplined experts")
    st.write(' 👉 Our driving instructors are licensed professionals')
    st.write('👉 Experienced drivers')
    st.write(' 👉 Well mannered and disciplined experts')
    st.write('📞 09481482060')
    st.write('\n**Operating Hours:**')
    st.write('Monday-Friday: 6 AM – 8 PM')
    st.write('Saturday: 6 AM – 8 PM')
    st.write('Sunday: Closed')

if selected=='location':
    st.title('SRINIVASA MOTOR DRIVING SCHOOL')
    # ✅ FIXED: Use relative paths
    st.image("location1.png", width=200)
    st.image("location2.png", width=200)
    st.header('Located at Srinivasa Reddy Building, Marathahalli Market')
    st.markdown('[🗺️ View on Google Maps](https://www.google.com/maps/place/Srinivasa+Motor+Driving+Training+School/@12.9555169,77.6919121,17z/data=!3m1!4b1!4m6!3m5!1s0x3bae13ceb881462d:0xda06fc705063ddb3!8m2!3d12.9555169!4d77.6919121!16s%2Fg%2F1v1tljcz?entry=ttu&g_ep=EgoyMDI1MDkwMy4wIKXMDSoASAFQAw%3D%3D)')

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
        st.write('Thank you for visiting, feel free to come back anytime!')

if selected == 'calendar':
    st.title('📅 Training Schedule Calendar')
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        year = st.number_input("Year:", min_value=2024, max_value=2030, value=2025)
        month = st.selectbox("Month:", range(1, 13), index=10, 
                           format_func=lambda x: calendar.month_name[x])
        
        cal = calendar.monthcalendar(year, month)
        
        st.write(f"### {calendar.month_name[month]} {year}")
        
        cols = st.columns(7)
        for i, day in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
            cols[i].markdown(f"**{day}**")
        
        for week in cal:
            cols = st.columns(7)
            for i, day in enumerate(week):
                if day == 0:
                    cols[i].write("")
                else:
                    if day in st.session_state.events:
                        cols[i].markdown(f"**:red[{day}]**")
                        cols[i].caption(f"📌 {st.session_state.events[day]}")
                    else:
                        cols[i].write(str(day))
    
    with col2:
        st.write("### ✏️ Manage Events")
        
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
        
        st.write("**All Events:**")
        if st.session_state.events:
            for day, event in sorted(st.session_state.events.items()):
                st.write(f"📅 Day {day}: {event}")
        else:
            st.info("No events scheduled")

if selected== 'blog':
    st.title("📝 Customer Feedback")
    name = st.text_input('Your Comments:')
    st.write(name)
    rate = st.slider('Rate us:', min_value=1, max_value=5)
    st.write(f"Rating: {rate}/5")
    for i in range(rate):
         st.write('⭐')
if selected=='mock test':
    video_file = open(r'video.mp4')
   video_bytes = video_file.read()
   st.video(video_bytes)







