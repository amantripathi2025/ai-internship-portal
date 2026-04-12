from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Your MongoDB connection
MONGO_URL = "mongodb+srv://amantripathi7550_db_user:xvta02cHxqLAV6s6@ai-internship-portal.ftfkc7h.mongodb.net/?appName=ai-internship-portal"

client = MongoClient(MONGO_URL, tlsAllowInvalidCertificates=True)
db = client["internship-portal"]
collection = db["internships"]

# 50+ Sample Internships
internships = [
    {
        "title": "Python Backend Developer",
        "company": "Tech Startup A",
        "location": "Bangalore",
        "requiredSkills": ["Python", "FastAPI", "MongoDB", "REST API"],
        "stipend": "₹15,000/month",
        "duration": "3 months",
        "description": "Build scalable backend services using Python and FastAPI",
        "applyLink": "https://example.com/apply/1"
    },
    {
        "title": "React Frontend Developer",
        "company": "Web Solutions Inc",
        "location": "Mumbai",
        "requiredSkills": ["React", "JavaScript", "Tailwind CSS", "Redux"],
        "stipend": "₹12,000/month",
        "duration": "3 months",
        "description": "Create responsive user interfaces with React",
        "applyLink": "https://example.com/apply/2"
    },
    {
        "title": "Java Full Stack Developer",
        "company": "Enterprise Systems",
        "location": "Delhi",
        "requiredSkills": ["Java", "Spring Boot", "MySQL", "REST API"],
        "stipend": "₹18,000/month",
        "duration": "4 months",
        "description": "Develop full-stack applications using Java and Spring Boot",
        "applyLink": "https://example.com/apply/3"
    },
    {
        "title": "Data Science Intern",
        "company": "AI Research Lab",
        "location": "Bangalore",
        "requiredSkills": ["Python", "Machine Learning", "Pandas", "NumPy"],
        "stipend": "₹16,000/month",
        "duration": "6 months",
        "description": "Work on machine learning projects and data analysis",
        "applyLink": "https://example.com/apply/4"
    },
    {
        "title": "DevOps Engineer",
        "company": "Cloud Services Ltd",
        "location": "Hyderabad",
        "requiredSkills": ["Docker", "Kubernetes", "AWS", "CI/CD"],
        "stipend": "₹17,000/month",
        "duration": "3 months",
        "description": "Manage cloud infrastructure and deployments",
        "applyLink": "https://example.com/apply/5"
    },
    {
        "title": "Mobile App Developer",
        "company": "Mobile Innovations",
        "location": "Bangalore",
        "requiredSkills": ["React Native", "JavaScript", "Firebase", "REST API"],
        "stipend": "₹14,000/month",
        "duration": "3 months",
        "description": "Develop cross-platform mobile applications",
        "applyLink": "https://example.com/apply/6"
    },
    {
        "title": "Database Administrator",
        "company": "Data Systems Corp",
        "location": "Mumbai",
        "requiredSkills": ["MongoDB", "MySQL", "Database Design", "SQL"],
        "stipend": "₹13,000/month",
        "duration": "3 months",
        "description": "Manage and optimize databases",
        "applyLink": "https://example.com/apply/7"
    },
    {
        "title": "QA Engineer",
        "company": "Quality Assurance Pro",
        "location": "Delhi",
        "requiredSkills": ["Selenium", "Testing", "JavaScript", "API Testing"],
        "stipend": "₹11,000/month",
        "duration": "3 months",
        "description": "Perform quality assurance and automated testing",
        "applyLink": "https://example.com/apply/8"
    },
    {
        "title": "Frontend Engineer",
        "company": "Design Studio",
        "location": "Bangalore",
        "requiredSkills": ["Vue.js", "JavaScript", "CSS", "HTML"],
        "stipend": "₹13,000/month",
        "duration": "4 months",
        "description": "Build beautiful user interfaces with Vue.js",
        "applyLink": "https://example.com/apply/9"
    },
    {
        "title": "Node.js Developer",
        "company": "Backend Experts",
        "location": "Pune",
        "requiredSkills": ["Node.js", "Express", "MongoDB", "REST API"],
        "stipend": "₹15,000/month",
        "duration": "3 months",
        "description": "Develop server-side applications with Node.js",
        "applyLink": "https://example.com/apply/10"
    },
    {
        "title": "AI/ML Engineer",
        "company": "AI Innovations",
        "location": "Bangalore",
        "requiredSkills": ["Python", "TensorFlow", "Deep Learning", "Data Science"],
        "stipend": "₹20,000/month",
        "duration": "6 months",
        "description": "Build AI and machine learning models",
        "applyLink": "https://example.com/apply/11"
    },
    {
        "title": "Cloud Engineer",
        "company": "AWS Solutions",
        "location": "Mumbai",
        "requiredSkills": ["AWS", "Docker", "Linux", "Cloud Architecture"],
        "stipend": "₹18,000/month",
        "duration": "4 months",
        "description": "Design and implement cloud solutions",
        "applyLink": "https://example.com/apply/12"
    },
    {
        "title": "Security Engineer",
        "company": "CyberSecurity Inc",
        "location": "Hyderabad",
        "requiredSkills": ["Cybersecurity", "Linux", "Network Security", "Penetration Testing"],
        "stipend": "₹19,000/month",
        "duration": "4 months",
        "description": "Ensure application and infrastructure security",
        "applyLink": "https://example.com/apply/13"
    },
    {
        "title": "Angular Developer",
        "company": "Enterprise Apps",
        "location": "Delhi",
        "requiredSkills": ["Angular", "TypeScript", "RxJS", "REST API"],
        "stipend": "₹14,000/month",
        "duration": "3 months",
        "description": "Build enterprise-grade web applications",
        "applyLink": "https://example.com/apply/14"
    },
    {
        "title": "GraphQL Developer",
        "company": "Modern Tech Stack",
        "location": "Bangalore",
        "requiredSkills": ["GraphQL", "Node.js", "React", "Apollo"],
        "stipend": "₹16,000/month",
        "duration": "3 months",
        "description": "Develop APIs using GraphQL",
        "applyLink": "https://example.com/apply/15"
    },
    {
        "title": "Microservices Developer",
        "company": "Distributed Systems",
        "location": "Bangalore",
        "requiredSkills": ["Microservices", "Spring Boot", "Docker", "Kubernetes"],
        "stipend": "₹17,000/month",
        "duration": "4 months",
        "description": "Build scalable microservices architecture",
        "applyLink": "https://example.com/apply/16"
    },
    {
        "title": "Blockchain Developer",
        "company": "Crypto Solutions",
        "location": "Mumbai",
        "requiredSkills": ["Solidity", "Blockchain", "Smart Contracts", "Web3"],
        "stipend": "₹21,000/month",
        "duration": "3 months",
        "description": "Develop blockchain and smart contract applications",
        "applyLink": "https://example.com/apply/17"
    },
    {
        "title": "Swift iOS Developer",
        "company": "iOS Apps Studio",
        "location": "Pune",
        "requiredSkills": ["Swift", "iOS Development", "Xcode", "Mobile UI"],
        "stipend": "₹14,000/month",
        "duration": "3 months",
        "description": "Develop native iOS applications",
        "applyLink": "https://example.com/apply/18"
    },
    {
        "title": "Kotlin Android Developer",
        "company": "Android Experts",
        "location": "Bangalore",
        "requiredSkills": ["Kotlin", "Android", "Java", "Firebase"],
        "stipend": "₹13,000/month",
        "duration": "3 months",
        "description": "Develop Android applications using Kotlin",
        "applyLink": "https://example.com/apply/19"
    },
    {
        "title": "Big Data Engineer",
        "company": "Data Analytics Corp",
        "location": "Mumbai",
        "requiredSkills": ["Spark", "Hadoop", "Python", "SQL"],
        "stipend": "₹18,000/month",
        "duration": "4 months",
        "description": "Work with big data technologies and analytics",
        "applyLink": "https://example.com/apply/20"
    },
    {
        "title": "PHP Developer",
        "company": "Web Development Studio",
        "location": "Delhi",
        "requiredSkills": ["PHP", "Laravel", "MySQL", "HTML/CSS"],
        "stipend": "₹11,000/month",
        "duration": "3 months",
        "description": "Develop web applications using PHP and Laravel",
        "applyLink": "https://example.com/apply/21"
    },
    {
        "title": "Rust Systems Developer",
        "company": "Systems Programming",
        "location": "Bangalore",
        "requiredSkills": ["Rust", "Systems Programming", "C++", "Low-level"],
        "stipend": "₹19,000/month",
        "duration": "4 months",
        "description": "Develop high-performance systems with Rust",
        "applyLink": "https://example.com/apply/22"
    },
    {
        "title": "Go Backend Developer",
        "company": "Performance Systems",
        "location": "Hyderabad",
        "requiredSkills": ["Go", "REST API", "Microservices", "Linux"],
        "stipend": "₹16,000/month",
        "duration": "3 months",
        "description": "Build high-performance backend services with Go",
        "applyLink": "https://example.com/apply/23"
    },
    {
        "title": "Technical Writer",
        "company": "Documentation Pro",
        "location": "Remote",
        "requiredSkills": ["Technical Writing", "API Documentation", "Markdown", "Git"],
        "stipend": "₹10,000/month",
        "duration": "3 months",
        "description": "Create technical documentation and API guides",
        "applyLink": "https://example.com/apply/24"
    },
    {
        "title": "DevOps with Terraform",
        "company": "Infrastructure Automation",
        "location": "Bangalore",
        "requiredSkills": ["Terraform", "AWS", "IaC", "CI/CD"],
        "stipend": "₹17,000/month",
        "duration": "3 months",
        "description": "Automate infrastructure with Terraform and AWS",
        "applyLink": "https://example.com/apply/25"
    },
    {
        "title": "React Native Developer",
        "company": "Cross-Platform Apps",
        "location": "Mumbai",
        "requiredSkills": ["React Native", "JavaScript", "Native Modules", "Mobile"],
        "stipend": "₹14,000/month",
        "duration": "3 months",
        "description": "Build cross-platform mobile apps with React Native",
        "applyLink": "https://example.com/apply/26"
    },
    {
        "title": "Backend with Python & Django",
        "company": "Django Development",
        "location": "Delhi",
        "requiredSkills": ["Python", "Django", "PostgreSQL", "REST API"],
        "stipend": "₹14,000/month",
        "duration": "3 months",
        "description": "Build robust backend services with Django",
        "applyLink": "https://example.com/apply/27"
    },
    {
        "title": "Frontend Vue Developer",
        "company": "Progressive Web Apps",
        "location": "Pune",
        "requiredSkills": ["Vue.js", "JavaScript", "Vuex", "CSS"],
        "stipend": "₹12,000/month",
        "duration": "3 months",
        "description": "Build progressive web applications with Vue.js",
        "applyLink": "https://example.com/apply/28"
    },
    {
        "title": "Database Optimization",
        "company": "Performance Experts",
        "location": "Bangalore",
        "requiredSkills": ["PostgreSQL", "Query Optimization", "Indexing", "SQL"],
        "stipend": "₹15,000/month",
        "duration": "3 months",
        "description": "Optimize database performance and queries",
        "applyLink": "https://example.com/apply/29"
    },
    {
        "title": "API Development",
        "company": "API First Company",
        "location": "Mumbai",
        "requiredSkills": ["REST API", "Node.js", "Express", "Swagger"],
        "stipend": "₹15,000/month",
        "duration": "3 months",
        "description": "Design and develop RESTful APIs",
        "applyLink": "https://example.com/apply/30"
    },
    {
        "title": "Testing Automation",
        "company": "Quality Masters",
        "location": "Delhi",
        "requiredSkills": ["Selenium", "Cypress", "Testing", "JavaScript"],
        "stipend": "₹12,000/month",
        "duration": "3 months",
        "description": "Automate software testing processes",
        "applyLink": "https://example.com/apply/31"
    },
    {
        "title": "Web Performance",
        "company": "Speed Optimizers",
        "location": "Bangalore",
        "requiredSkills": ["Web Performance", "JavaScript", "React", "CDN"],
        "stipend": "₹14,000/month",
        "duration": "3 months",
        "description": "Optimize web application performance",
        "applyLink": "https://example.com/apply/32"
    },
    {
        "title": "Accessibility Developer",
        "company": "Inclusive Tech",
        "location": "Mumbai",
        "requiredSkills": ["WCAG", "Accessibility", "HTML/CSS", "Testing"],
        "stipend": "₹13,000/month",
        "duration": "3 months",
        "description": "Ensure web accessibility standards compliance",
        "applyLink": "https://example.com/apply/33"
    },
    {
        "title": "WebAssembly Developer",
        "company": "Web Performance Lab",
        "location": "Hyderabad",
        "requiredSkills": ["WebAssembly", "Rust", "JavaScript", "Performance"],
        "stipend": "₹17,000/month",
        "duration": "4 months",
        "description": "Develop high-performance web applications with WebAssembly",
        "applyLink": "https://example.com/apply/34"
    },
    {
        "title": "Cloud Storage Developer",
        "company": "Storage Solutions",
        "location": "Bangalore",
        "requiredSkills": ["Cloud Storage", "AWS S3", "Python", "Distributed Systems"],
        "stipend": "₹16,000/month",
        "duration": "3 months",
        "description": "Build cloud storage applications",
        "applyLink": "https://example.com/apply/35"
    },
    {
        "title": "Monitoring & Observability",
        "company": "DevOps Monitoring",
        "location": "Delhi",
        "requiredSkills": ["Prometheus", "Grafana", "ELK Stack", "Logging"],
        "stipend": "₹16,000/month",
        "duration": "3 months",
        "description": "Implement monitoring and observability solutions",
        "applyLink": "https://example.com/apply/36"
    },
    {
        "title": "Serverless Developer",
        "company": "Serverless Architecture",
        "location": "Mumbai",
        "requiredSkills": ["AWS Lambda", "Serverless Framework", "Node.js", "Python"],
        "stipend": "₹15,000/month",
        "duration": "3 months",
        "description": "Build serverless applications on AWS Lambda",
        "applyLink": "https://example.com/apply/37"
    },
    {
        "title": "Rate Limiting Developer",
        "company": "API Gateway Solutions",
        "location": "Bangalore",
        "requiredSkills": ["Rate Limiting", "Redis", "API Gateway", "Performance"],
        "stipend": "₹14,000/month",
        "duration": "3 months",
        "description": "Implement rate limiting and API throttling",
        "applyLink": "https://example.com/apply/38"
    },
    {
        "title": "Email Service Developer",
        "company": "Communication Systems",
        "location": "Pune",
        "requiredSkills": ["Email Services", "SMTP", "Node.js", "AWS SES"],
        "stipend": "₹12,000/month",
        "duration": "3 months",
        "description": "Build email service integrations",
        "applyLink": "https://example.com/apply/39"
    },
    {
        "title": "Payment Gateway Integration",
        "company": "Fintech Solutions",
        "location": "Mumbai",
        "requiredSkills": ["Payment APIs", "Stripe", "PCI Compliance", "Node.js"],
        "stipend": "₹16,000/month",
        "duration": "4 months",
        "description": "Integrate payment gateways and handle transactions",
        "applyLink": "https://example.com/apply/40"
    },
    {
        "title": "Real-time Applications",
        "company": "WebSocket Experts",
        "location": "Bangalore",
        "requiredSkills": ["WebSocket", "Socket.io", "Node.js", "Real-time"],
        "stipend": "₹15,000/month",
        "duration": "3 months",
        "description": "Build real-time web applications",
        "applyLink": "https://example.com/apply/41"
    },
    {
        "title": "Message Queue Developer",
        "company": "Async Systems",
        "location": "Delhi",
        "requiredSkills": ["RabbitMQ", "Kafka", "Message Queues", "Python"],
        "stipend": "₹16,000/month",
        "duration": "3 months",
        "description": "Work with message queue systems",
        "applyLink": "https://example.com/apply/42"
    },
    {
        "title": "Search Engine Developer",
        "company": "Elasticsearch Experts",
        "location": "Mumbai",
        "requiredSkills": ["Elasticsearch", "Search", "Lucene", "Python"],
        "stipend": "₹15,000/month",
        "duration": "3 months",
        "description": "Implement search functionality with Elasticsearch",
        "applyLink": "https://example.com/apply/43"
    },
    {
        "title": "Caching Specialist",
        "company": "Performance Optimization",
        "location": "Hyderabad",
        "requiredSkills": ["Redis", "Caching", "Memcached", "Performance"],
        "stipend": "₹14,000/month",
        "duration": "3 months",
        "description": "Implement caching strategies with Redis",
        "applyLink": "https://example.com/apply/44"
    },
    {
        "title": "Load Balancing Engineer",
        "company": "Infrastructure Services",
        "location": "Bangalore",
        "requiredSkills": ["Load Balancing", "Nginx", "HAProxy", "DevOps"],
        "stipend": "₹15,000/month",
        "duration": "3 months",
        "description": "Configure and optimize load balancing",
        "applyLink": "https://example.com/apply/45"
    },
    {
        "title": "Database Sharding",
        "company": "Scalable Systems",
        "location": "Delhi",
        "requiredSkills": ["Database Sharding", "MongoDB", "Distribution", "SQL"],
        "stipend": "₹17,000/month",
        "duration": "4 months",
        "description": "Implement database sharding for scalability",
        "applyLink": "https://example.com/apply/46"
    },
    {
        "title": "Container Orchestration",
        "company": "Kubernetes Experts",
        "location": "Mumbai",
        "requiredSkills": ["Kubernetes", "Docker", "Helm", "Container Orchestration"],
        "stipend": "₹18,000/month",
        "duration": "4 months",
        "description": "Manage containerized applications with Kubernetes",
        "applyLink": "https://example.com/apply/47"
    },
    {
        "title": "API Gateway Developer",
        "company": "Gateway Solutions",
        "location": "Bangalore",
        "requiredSkills": ["API Gateway", "Kong", "Authentication", "Rate Limiting"],
        "stipend": "₹16,000/month",
        "duration": "3 months",
        "description": "Build API gateways and middleware",
        "applyLink": "https://example.com/apply/48"
    },
    {
        "title": "Service Mesh Developer",
        "company": "Istio Experts",
        "location": "Pune",
        "requiredSkills": ["Istio", "Service Mesh", "Kubernetes", "Networking"],
        "stipend": "₹17,000/month",
        "duration": "4 months",
        "description": "Implement service mesh architecture",
        "applyLink": "https://example.com/apply/49"
    },
    {
        "title": "Configuration Management",
        "company": "Infrastructure Automation",
        "location": "Delhi",
        "requiredSkills": ["Ansible", "Configuration Management", "Linux", "YAML"],
        "stipend": "₹14,000/month",
        "duration": "3 months",
        "description": "Manage infrastructure configuration",
        "applyLink": "https://example.com/apply/50"
    },
    {
        "title": "Log Aggregation",
        "company": "Observability Platform",
        "location": "Mumbai",
        "requiredSkills": ["ELK Stack", "Logstash", "Kibana", "Logging"],
        "stipend": "₹15,000/month",
        "duration": "3 months",
        "description": "Build centralized logging solutions",
        "applyLink": "https://example.com/apply/51"
    },
    {
        "title": "Distributed Tracing",
        "company": "APM Solutions",
        "location": "Bangalore",
        "requiredSkills": ["Jaeger", "Distributed Tracing", "APM", "Observability"],
        "stipend": "₹16,000/month",
        "duration": "3 months",
        "description": "Implement distributed tracing systems",
        "applyLink": "https://example.com/apply/52"
    },
    {
        "title": "Incident Response",
        "company": "DevOps Culture",
        "location": "Hyderabad",
        "requiredSkills": ["Incident Management", "On-call", "Response", "Automation"],
        "stipend": "₹14,000/month",
        "duration": "3 months",
        "description": "Build incident response and alerting systems",
        "applyLink": "https://example.com/apply/53"
    },
]

# Delete old data if exists
collection.delete_many({})

# Insert all internships
result = collection.insert_many(internships)

print(f"✅ Successfully added {len(result.inserted_ids)} internships to the database!")
print(f"📊 Database: internship-portal")
print(f"📝 Collection: internships")