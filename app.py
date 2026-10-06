import streamlit as st

from modules.ai_engine import AIEngine
from modules.answer_evaluator import AnswerEvaluator
from modules.database import InterviewDatabase
from modules.resume_parser import ResumeParser


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Interview Preparation System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f4f8ff 0%, #ffffff 100%);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f4c81, #2563eb);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    .home-hero {
        background: linear-gradient(135deg, #0f4c81, #2563eb, #38bdf8);
        padding: 45px 35px;
        border-radius: 24px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 12px 35px rgba(37, 99, 235, 0.25);
    }

    .home-hero h1 {
        color: white !important;
        font-size: 42px;
        margin: 8px 0;
    }

    .home-hero h3 {
        color: white !important;
        font-size: 22px;
        font-weight: 500;
        margin: 8px 0 16px 0;
    }

    .home-hero p {
        color: white !important;
        font-size: 17px;
        line-height: 1.7;
        max-width: 900px;
        margin: auto;
    }

    .section-title {
        color: #0f4c81;
        font-size: 28px;
        font-weight: 700;
        margin: 28px 0 16px 0;
    }

    .card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        min-height: 175px;
        margin-bottom: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.07);
    }

    .card h3 {
        color: #1e3a8a !important;
        margin-bottom: 8px;
    }

    .card p {
        color: #555 !important;
        line-height: 1.6;
    }

    .info-box {
        background: #eff6ff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #2563eb;
        margin: 15px 0;
    }

    .success-box {
        background: #ecfdf5;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #10b981;
        margin: 15px 0;
    }

    .cta-box {
        background: linear-gradient(135deg, #1e3a8a, #2563eb);
        color: white;
        padding: 32px;
        border-radius: 22px;
        text-align: center;
        margin: 30px 0;
    }

    .cta-box h2,
    .cta-box p {
        color: white !important;
    }

    .footer {
        text-align: center;
        padding: 24px;
        color: #666;
        font-size: 14px;
        border-top: 1px solid #ddd;
        margin-top: 35px;
    }

    div.stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# INITIALIZE SYSTEM
# ============================================================

@st.cache_resource
def initialize_system():
    ai_engine = AIEngine()
    answer_evaluator = AnswerEvaluator(ai_engine)
    database = InterviewDatabase()
    resume_parser = ResumeParser()

    return ai_engine, answer_evaluator, database, resume_parser


try:
    ai_engine, answer_evaluator, database, resume_parser = initialize_system()
except Exception as e:
    st.error("Unable to initialize the application.")
    st.exception(e)
    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding:15px;">
            <div style="font-size:55px;">🎯</div>
            <h2>AI Interview Coach</h2>
            <p>Prepare • Practice • Improve • Succeed</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.subheader("📌 Main Menu")

    menu = st.radio(
        "Navigate",
        [
            "🏠 Home",
            "📄 Resume Analysis",
            "❓ Generate Questions",
            "🎤 Practice Interview",
            "📊 Performance",
            "ℹ️ About",
        ],
        index=0,
        key="main_menu",
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center; padding:10px;">
            <h4>🚀 Preparation Cycle</h4>
            <p>📄 Resume</p>
            <p>⬇️</p>
            <p>❓ Questions</p>
            <p>⬇️</p>
            <p>🎤 Practice</p>
            <p>⬇️</p>
            <p>📊 Evaluate</p>
            <p>⬇️</p>
            <p>🏆 Improve</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HOME PAGE
# IMPORTANT:
# The Home page intentionally uses Streamlit components instead
# of large raw HTML blocks. This prevents the HTML source from
# appearing as plain text in the application.
# ============================================================

if menu == "🏠 Home":

    st.markdown(
        """
        <div class="home-hero">
            <div style="font-size:65px;">🎯</div>
            <h1>AI Interview Preparation System</h1>
            <h3>Your Personal AI-Powered Interview Coach</h3>
            <p>
                Prepare for your dream job with intelligent resume analysis,
                personalized interview questions, mock interview practice,
                AI-powered answer evaluation and performance tracking.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-box">
            <h3>👋 Welcome to Your Interview Preparation Platform!</h3>
            <p>
                This system helps students and job seekers prepare for
                interviews in a structured and intelligent way. Upload your
                resume, generate interview questions, practice your answers
                and evaluate your performance.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">⚡ What You Can Do</div>',
        unsafe_allow_html=True,
    )

    features = [
        (
            "📄",
            "Smart Resume Analysis",
            "Upload your resume and extract important information to prepare interview questions based on your profile.",
        ),
        (
            "❓",
            "AI Question Generation",
            "Generate technical, HR and behavioral questions according to your selected job role and experience.",
        ),
        (
            "🎤",
            "Mock Interview",
            "Practice interview questions and improve your confidence before attending a real interview.",
        ),
        (
            "🤖",
            "AI Answer Evaluation",
            "Get a score, strengths, weaknesses and suggestions for improving your interview answers.",
        ),
        (
            "📊",
            "Performance Tracking",
            "Review your previous interview attempts and understand how your preparation is progressing.",
        ),
        (
            "🏆",
            "Improve Your Confidence",
            "Practice repeatedly, learn from feedback and become more confident for your real interview.",
        ),
    ]

    feature_columns = st.columns(3)

    for i, (icon, title, description) in enumerate(features):
        with feature_columns[i % 3]:
            with st.container(border=True):
                st.markdown(f"### {icon} {title}")
                st.write(description)

    st.markdown(
        '<div class="section-title">🔄 How It Works</div>',
        unsafe_allow_html=True,
    )

    process = [
        (
            "01",
            "Upload Resume",
            "Upload your PDF resume and extract your professional information.",
        ),
        (
            "02",
            "Generate Questions",
            "Select your job role, experience and question type to generate interview questions.",
        ),
        (
            "03",
            "Practice",
            "Answer interview questions and practice explaining your knowledge.",
        ),
        (
            "04",
            "Get Feedback",
            "Receive an evaluation and suggestions to improve your answers.",
        ),
    ]

    process_columns = st.columns(4)

    for i, (number, title, description) in enumerate(process):
        with process_columns[i]:
            with st.container(border=True):
                st.markdown(f"## {number}")
                st.markdown(f"### {title}")
                st.write(description)

    st.markdown(
        '<div class="section-title">🎓 Interview Types</div>',
        unsafe_allow_html=True,
    )

    interview_types = [
        (
            "💻",
            "Technical Interview",
            "Practice questions related to programming, technologies, projects and technical concepts.",
        ),
        (
            "👔",
            "HR Interview",
            "Prepare answers for questions about yourself, strengths, weaknesses, career goals and motivation.",
        ),
        (
            "🧠",
            "Behavioral Interview",
            "Practice real-world situation questions using structured methods such as the STAR technique.",
        ),
    ]

    type_columns = st.columns(3)

    for i, (icon, title, description) in enumerate(interview_types):
        with type_columns[i]:
            with st.container(border=True):
                st.markdown(f"### {icon} {title}")
                st.write(description)

    st.markdown(
        '<div class="section-title">💡 Interview Preparation Tips</div>',
        unsafe_allow_html=True,
    )

    tips_col1, tips_col2 = st.columns(2)

    with tips_col1:
        st.markdown(
            """
            <div class="info-box">
                <h4>✅ Before the Interview</h4>
                <ul>
                    <li>Research the company.</li>
                    <li>Understand the job description.</li>
                    <li>Review your resume.</li>
                    <li>Practice common questions.</li>
                    <li>Prepare questions for the interviewer.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tips_col2:
        st.markdown(
            """
            <div class="success-box">
                <h4>🎯 During the Interview</h4>
                <ul>
                    <li>Speak clearly and confidently.</li>
                    <li>Listen carefully to questions.</li>
                    <li>Give specific examples.</li>
                    <li>Use the STAR method for behavioral questions.</li>
                    <li>Stay positive and professional.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="cta-box">
            <h2>🚀 Ready to Start Your Preparation?</h2>
            <p>
                Start with your resume, generate personalized questions,
                practice your answers and improve your interview skills.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="footer">
            🎯 AI Interview Preparation System<br><br>
            Prepare • Practice • Improve • Succeed<br><br>
            Developed using Python and Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# RESUME ANALYSIS
# ============================================================

elif menu == "📄 Resume Analysis":

    st.title("📄 Resume Analysis")

    st.write(
        "Upload your resume in PDF format to extract and analyze your information."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"],
    )

    if uploaded_file is not None:

        if st.button("🔍 Analyze Resume"):

            with st.spinner("Reading your resume..."):

                try:
                    resume_text = resume_parser.extract_text(uploaded_file)

                    if resume_text.strip():

                        st.success(
                            "✅ Resume uploaded and analyzed successfully!"
                        )

                        st.subheader("📋 Extracted Resume Content")

                        st.text_area(
                            "Resume Text",
                            resume_text,
                            height=400,
                        )

                        st.session_state["resume_text"] = resume_text

                    else:
                        st.warning(
                            "⚠️ No readable text was found in the PDF."
                        )

                except Exception as e:
                    st.error(f"❌ Error while reading resume: {e}")


# ============================================================
# GENERATE QUESTIONS
# ============================================================

elif menu == "❓ Generate Questions":

    st.title("❓ Interview Question Generator")

    st.write(
        "Generate interview questions based on your job role and experience."
    )

    col1, col2 = st.columns(2)

    with col1:

        job_role = st.text_input(
            "💼 Job Role",
            placeholder="Example: Python Developer",
        )

        experience = st.selectbox(
            "📈 Experience Level",
            [
                "Fresher",
                "0-1 Years",
                "1-3 Years",
                "3-5 Years",
                "5+ Years",
            ],
        )

    with col2:

        question_type = st.selectbox(
            "📝 Question Type",
            [
                "Technical",
                "HR",
                "Behavioral",
                "Mixed",
            ],
        )

        number_of_questions = st.slider(
            "🔢 Number of Questions",
            min_value=1,
            max_value=10,
            value=5,
        )

    if st.button("🚀 Generate Questions"):

        if not job_role.strip():

            st.warning("⚠️ Please enter a job role.")

        else:

            try:
                with st.spinner("Generating questions..."):

                    questions = ai_engine.generate_questions(
                        job_role,
                        experience,
                        question_type,
                        number_of_questions,
                    )

                st.success(f"✅ Generated {len(questions)} questions!")

                st.session_state["questions"] = questions

                for index, question in enumerate(questions, start=1):

                    with st.container(border=True):
                        st.markdown(f"### Question {index}")
                        st.write(question)

            except Exception as e:
                st.error(f"❌ Unable to generate questions: {e}")


# ============================================================
# PRACTICE INTERVIEW
# ============================================================

elif menu == "🎤 Practice Interview":

    st.title("🎤 Mock Interview Practice")

    st.write(
        "Practice your interview answers and receive AI-powered feedback."
    )

    questions = st.session_state.get("questions", [])

    if not questions:

        st.info(
            "ℹ️ First go to 'Generate Questions' and create some interview questions."
        )

    else:

        question_number = st.selectbox(
            "Select Question",
            range(1, len(questions) + 1),
        )

        current_question = questions[question_number - 1]

        st.markdown(
            f"""
            <div class="info-box">
                <h3>❓ Interview Question</h3>
                <p style="font-size:18px;">{current_question}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        answer = st.text_area(
            "✍️ Your Answer",
            height=220,
            placeholder="Type your interview answer here...",
        )

        if st.button("🤖 Evaluate My Answer"):

            if not answer.strip():

                st.warning("⚠️ Please enter your answer first.")

            else:

                try:

                    with st.spinner("AI is evaluating your answer..."):

                        evaluation = answer_evaluator.evaluate(
                            current_question,
                            answer,
                        )

                    st.success("✅ Evaluation completed!")

                    st.subheader("📊 AI Evaluation")
                    st.markdown(evaluation)

                    try:

                        database.save_interview(
                            current_question,
                            answer,
                            evaluation,
                        )

                        st.success(
                            "💾 Interview attempt saved successfully!"
                        )

                    except Exception as e:
                        st.error(f"Database error: {e}")

                except Exception as e:
                    st.error(f"❌ Unable to evaluate the answer: {e}")


# ============================================================
# PERFORMANCE
# ============================================================

elif menu == "📊 Performance":

    st.title("📊 Performance Dashboard")

    st.write(
        "Review your previous interview practice sessions."
    )

    try:

        interviews = database.get_all_interviews()

        if not interviews:

            st.info("📭 No interview attempts found yet.")

            st.write(
                "Complete a mock interview to see your performance here."
            )

        else:

            st.success(
                f"🎯 Total Practice Attempts: {len(interviews)}"
            )

            for index, interview in enumerate(
                interviews,
                start=1,
            ):

                with st.expander(
                    f"Interview Attempt {index} - {interview['date']}"
                ):

                    st.markdown("**❓ Question:**")
                    st.write(interview["question"])

                    st.markdown("**✍️ Your Answer:**")
                    st.write(interview["answer"])

                    st.markdown("**🤖 AI Evaluation:**")
                    st.markdown(interview["evaluation"])

    except Exception as e:

        st.error(
            f"Unable to load performance data: {e}"
        )


# ============================================================
# ABOUT
# ============================================================

elif menu == "ℹ️ About":

    st.title("ℹ️ About the Project")

    st.markdown(
        """
        <div class="home-hero">
            <div style="font-size:60px;">🎯</div>
            <h1>AI Interview Preparation System</h1>
            <h3>Intelligent Interview Preparation Platform</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("📌 Project Overview")

    st.write(
        """
        The AI Interview Preparation System is designed to help students
        and job seekers prepare for technical, HR and behavioral interviews.

        The system provides resume analysis, interview question generation,
        mock interview practice, answer evaluation and performance tracking.
        """
    )

    st.subheader("🎯 Main Objectives")

    objectives = [
        "Analyze candidate resumes.",
        "Generate relevant interview questions.",
        "Provide mock interview practice.",
        "Evaluate candidate answers.",
        "Provide improvement suggestions.",
        "Store previous interview attempts.",
        "Help candidates improve interview confidence.",
    ]

    for objective in objectives:
        st.write(f"✅ {objective}")

    st.subheader("🛠️ Technologies Used")

    tech_columns = st.columns(4)

    technologies = [
        ("🐍", "Python", "Main programming language."),
        ("🎨", "Streamlit", "Web application framework."),
        ("📄", "PyPDF", "Used for reading PDF resumes."),
        ("🗄️", "SQLite", "Used for storing interview attempts."),
    ]

    for i, (icon, name, description) in enumerate(technologies):

        with tech_columns[i]:

            with st.container(border=True):
                st.markdown(f"### {icon} {name}")
                st.write(description)

    st.markdown(
        """
        <div class="footer">
            🎯 AI Interview Preparation System<br><br>
            Prepare • Practice • Improve • Succeed
        </div>
        """,
        unsafe_allow_html=True,
    )
