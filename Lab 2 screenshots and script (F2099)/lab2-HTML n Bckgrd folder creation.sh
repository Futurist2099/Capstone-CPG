#!/bin/bash
# =============================================================================
# Lab 2: EC2 Startup Script (User Data Automation)
# Author: TJerome (F2099)
# Purpose: Automatically configure an EC2 instance to host a static website
# Web Server: Apache (httpd)
# =============================================================================

# -----------------------------------------------------------------------------
# STEP 1: System Update
# Ensures all packages are current before installing new software
# -----------------------------------------------------------------------------
yum update -y

# -----------------------------------------------------------------------------
# STEP 2: Install Apache Web Server
# httpd is the Apache package name on Amazon Linux
# -----------------------------------------------------------------------------
yum install -y httpd

# -----------------------------------------------------------------------------
# STEP 3: Start Apache and Enable Auto-Start on Boot
# systemctl start  → starts the service immediately
# systemctl enable → ensures it starts automatically after reboot
# -----------------------------------------------------------------------------
systemctl start httpd
systemctl enable httpd

# -----------------------------------------------------------------------------
# STEP 4: Create the HTML Web Page
# This writes a complete HTML file with inline CSS to the Apache web root
# The page includes: name, background image, embedded image, and 3 sections
# -----------------------------------------------------------------------------
cat <<'EOF' > /var/www/html/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> TJerome (F2099) | EC2 Static Site</title>
    <style>
        /* ===== GLOBAL STYLES ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.8;
            color: #f0f0f0;
            background-image: url('https://static.vecteezy.com/system/resources/previews/068/351/056/non_2x/thailand-japan-flags-crossed-image-free-vector.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            min-height: 100vh;
        }

        /* ===== OVERLAY FOR READABILITY ===== */
        .overlay {
            background-color: rgba(0, 0, 0, 0.7);
            min-height: 100vh;
            padding: 40px 20px;
        }

        /* ===== CONTAINER ===== */
        .container {
            max-width: 900px;
            margin: 0 auto;
        }

        /* ===== HEADER ===== */
        header {
            text-align: center;
            padding: 40px 0;
            border-bottom: 2px solid rgba(255, 255, 255, 0.2);
            margin-bottom: 40px;
        }

        header h1 {
            font-size: 3rem;
            color: #00d4ff;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
            margin-bottom: 10px;
        }

        header p {
            font-size: 1.2rem;
            color: #b0b0b0;
            font-style: italic;
        }

        /* ===== CONTENT SECTIONS ===== */
        .section {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .section h2 {
            color: #00d4ff;
            font-size: 1.8rem;
            margin-bottom: 15px;
            border-left: 4px solid #00d4ff;
            padding-left: 15px;
        }

        .section p {
            font-size: 1.1rem;
            color: #e0e0e0;
        }

        /* ===== EMBEDDED IMAGE ===== */
        .image-container {
            text-align: center;
            margin: 30px 0;
        }

        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            border: 2px solid rgba(0, 212, 255, 0.3);
        }

        .image-container p {
            margin-top: 10px;
            font-size: 0.9rem;
            color: #888;
            font-style: italic;
        }

        /* ===== FOOTER ===== */
        footer {
            text-align: center;
            padding: 30px 0;
            margin-top: 40px;
            border-top: 2px solid rgba(255, 255, 255, 0.2);
        }

        footer p {
            color: #888;
            font-size: 1rem;
        }

        footer .copyright {
            margin-top: 15px;
            font-size: 0.9rem;
            color: #667;
        }
    </style>
</head>
<body>
    <div class="overlay">
        <div class="container">
            
            <!-- HEADER WITH NAME -->
            <header>
                <h1> TJerome (F2099)</h1>
                <p>Tech guy | Car nut</p>
            </header>

            <!-- SECTION 1: ABOUT ME -->
            <section class="section">
                <h2>About Me</h2>
                <p> Learning to level up one day at a time. </p>
            </section>

            <!-- EMBEDDED IMAGE -->
            <div class="image-container">
                <img src="https://media1.tenor.com/m/qG7IOtZ4d3MAAAAC/ae86-brake.gif">
                <p> Do what it takes </p>
            </div>

            <!-- SECTION 2: PROJECT DESCRIPTION -->
            <section class="section">
                <h2>Project Description</h2>
                <p>This lab introduces AWS EC2 initialization by writing a startup / background folder creation script that configures an EC2 instance to host a front-facing static website followed by a backup job running in the background.</p>
            </section>

            <!-- SECTION 3: CONTACT -->
            <section class="section">
                <h2>Contact</h2>
                <p>Questions, collaborations, or inquiries? Find me on Discord.</p>
            </section>

            <!-- FOOTER -->
            <footer>
                <p> Capstone L2, Summer 2026.</p>
            </footer>

        </div>
    </div>
</body>
</html>
EOF

creates CSS file
cat > /var/www/html/style.css << EOF

body {
    background-color: grey;
    text-align: center;
    font-family: Times New Roman, serif;
}

h1 {
    color: black;
}

h2 {
    color: white;
}

EOF

@reboot

mkdir /home/ec2-user/test1
mkdir /home/ec2-user/lz_backup

base_dir="/home/ec2-user/test1"
backup_dir="/home/ec2-user/lz_backup"

echo "Report copy1 in progress" >> "$base_dir"/report1.txt
echo "Report copy2 in progress" >> "$base_dir"/report2.txt
echo "Report copy3 in progress" >> "$base_dir"/report3.txt
echo "Report copy4 in progress" >> "$base_dir"/report4.txt



cp -v  "$base_dir"/rep*.txt  "$backup_dir"
 
echo "4 file copy batch in progress" >> "$base_dir"/report_final.txt



mkdir /home/ec2-user/content
cont_dir="/home/ec2-user/content"
echo "Content copy1 in progress" >> "$cont_dir"/report-ct.txt

mkdir /home/ec2-user/utils
utils_dir="/home/ec2-user/utils"
echo "Utils copy1 in progress" >> "$utils_dir"/report-ul.txt

mkdir /home/ec2-user/credentials
creds_dir="/home/ec2-user/credentials"
echo "Credentials copy1 in progress" >> "$creds_dir"/report-cr.txt
