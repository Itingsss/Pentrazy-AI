import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime

fake = Faker()

# Set seed untuk reproducibility
random.seed(42)
np.random.seed(42)

# Jumlah data yang ingin dibuat
TOTAL_DATA = 5000

# Data dasar untuk pertanyaan pemrograman
programming_languages = ['Python', 'JavaScript', 'Java', 'C++', 'C#', 'PHP', 'Ruby', 'Go', 'Swift', 'Kotlin']
programming_topics = {
    'syntax': ['cara membuat', 'sintaks untuk', 'contoh', 'bagaimana', 'apa itu'],
    'error': ['memperbaiki error', 'menyelesaikan masalah', 'debugging', 'troubleshoot'],
    'concept': ['penjelasan tentang', 'pengertian', 'konsep dasar', 'cara kerja'],
    'tool': ['menggunakan', 'setup', 'konfigurasi', 'integrasi']
}

# Data dasar untuk pertanyaan cybersecurity
cybersecurity_topics = {
    'pentesting': ['metode', 'tools', 'langkah-langkah', 'teknik dasar', 'best practice'],
    'network': ['keamanan jaringan', 'serangan jaringan', 'pertahanan jaringan', 'monitoring'],
    'web': ['keamanan web', 'serangan SQLi', 'XSS', 'CSRF', 'keamanan API'],
    'cryptography': ['enkripsi', 'dekripsi', 'algoritma', 'implementasi'],
    'malware': ['analisis malware', 'jenis malware', 'pencegahan', 'deteksi']
}

# Fungsi untuk membuat pertanyaan pemrograman
def generate_programming_question():
    lang = random.choice(programming_languages)
    topic = random.choice(list(programming_topics.keys()))
    subtopic = random.choice(programming_topics[topic])
    
    questions = {
        'syntax': [
            f"{subtopic} {lang}?",
            f"{subtopic} di {lang}?",
            f"Bagaimana {subtopic} dalam {lang}?"
        ],
        'error': [
            f"Cara {subtopic} di {lang}?",
            f"{subtopic} {lang}?",
            f"Solusi untuk {subtopic} {lang}?"
        ],
        'concept': [
            f"Bisa jelaskan {subtopic} {lang}?",
            f"Apa itu {subtopic} {lang}?",
            f"Bagaimana {subtopic} {lang} bekerja?"
        ],
        'tool': [
            f"Cara {subtopic} {lang}?",
            f"Tutorial {subtopic} {lang}",
            f"Panduan {subtopic} {lang}"
        ]
    }
    
    return random.choice(questions[topic])

# Fungsi untuk membuat jawaban pemrograman
def generate_programming_answer(question):
    if '?' in question:
        question = question.replace('?', '')
    
    if 'Python' in question:
        if 'cara membuat' in question or 'sintaks untuk' in question:
            return f"Di Python, Anda bisa menggunakan sintaks berikut:\n\n```python\n# Contoh kode\nfor i in range(10):\n    print(i)\n```\n\nPastikan indentasi yang benar."
        elif 'error' in question or 'masalah' in question:
            return f"Untuk masalah di Python, coba periksa:\n1. Indentasi\n2. Import module\n3. Error message\n4. Versi Python\n\n{random.choice(['Coba gunakan try-except.', 'Periksa dokumentasi resmi.'])}"
    
    elif 'JavaScript' in question:
        if 'function' in question or 'fungsi' in question:
            return "Di JavaScript, fungsi dapat dibuat dengan:\n\n```javascript\nfunction namaFungsi(parameter) {\n  // kode\n  return hasil;\n}\n\n// Atau arrow function\nconst namaFungsi = (param) => { /* kode */ };\n```"
    
    # Jawaban umum untuk pemrograman
    templates = [
        f"Untuk {question}, Anda bisa menggunakan:\n```\n// Contoh kode\nint main() {{\n  return 0;\n}}\n```",
        f"{question} adalah konsep penting dalam pemrograman. Berikut penjelasannya:\n\n- Poin 1\n- Poin 2\n- Poin 3",
        f"Untuk menyelesaikan {question}, ikuti langkah berikut:\n1. Langkah pertama\n2. Langkah kedua\n3. Langkah ketiga\n\nReferensi: {fake.url()}",
        f"Error tersebut biasanya terjadi karena:\n- Penyebab 1\n- Penyebab 2\n\nSolusi:\n- Solusi 1\n- Solusi 2"
    ]
    
    return random.choice(templates)

# Fungsi untuk membuat pertanyaan cybersecurity
def generate_cybersecurity_question():
    topic = random.choice(list(cybersecurity_topics.keys()))
    subtopic = random.choice(cybersecurity_topics[topic])
    
    questions = {
        'pentesting': [
            f"Apa {subtopic} pentesting?",
            f"Bagaimana {subtopic} dalam pentesting?",
            f"Tools untuk {subtopic} pentesting?",
            f"Metode {subtopic} saat pentesting"
        ],
        'network': [
            f"Cara mengamankan {subtopic}?",
            f"{subtopic} yang efektif?",
            f"Deteksi {subtopic}?",
            f"Serangan {subtopic} umum?"
        ],
        'web': [
            f"Pencegahan {subtopic}?",
            f"Contoh {subtopic}?",
            f"Tools untuk {subtopic}?",
            f"Analisis {subtopic}?"
        ],
        'cryptography': [
            f"Implementasi {subtopic}?",
            f"Algoritma {subtopic} terbaik?",
            f"Konsep {subtopic}?",
            f"Contoh {subtopic} praktis?"
        ],
        'malware': [
            f"Deteksi {subtopic}?",
            f"Analisis {subtopic}?",
            f"Pencegahan {subtopic}?",
            f"Tools {subtopic} terbaik?"
        ]
    }
    
    return random.choice(questions[topic])

# Fungsi untuk membuat jawaban cybersecurity
def generate_cybersecurity_answer(question):
    if 'pentesting' in question:
        return f"Dalam pentesting, {question.lower().replace('?', '')} meliputi:\n\n- {fake.sentence()}\n- {fake.sentence()}\n- Tools yang bisa digunakan: {random.choice(['Nmap', 'Metasploit', 'Burp Suite', 'Wireshark'])}\n\nReferensi: {fake.url()}"
    
    elif 'network' in question:
        return f"Untuk keamanan jaringan:\n\n1. {fake.sentence()}\n2. {fake.sentence()}\n3. Protokol yang direkomendasikan: {random.choice(['TLS 1.3', 'IPSec', 'WPA3'])}\n\n{random.choice(['Selalu update firmware.', 'Gunakan firewall yang tepat.'])}"
    
    elif 'web' in question:
        return f"Keamanan web penting untuk:\n- {fake.sentence()}\n- {fake.sentence()}\n\nTools pentesting web: {random.choice(['OWASP ZAP', 'Burp Suite', 'Nikto'])}\n\nTips: {fake.sentence()}"
    
    elif 'cryptography' in question:
        return f"Kriptografi {question.lower().replace('?', '')}:\n\nAlgoritma: {random.choice(['AES', 'RSA', 'ECDSA', 'SHA-256'])}\n\nImplementasi:\n```python\nfrom cryptography.fernet import Fernet\nkey = Fernet.generate_key()\n```"
    
    elif 'malware' in question:
        return f"Malware analysis meliputi:\n1. Static analysis\n2. Dynamic analysis\n\nTools: {random.choice(['IDA Pro', 'Ghidra', 'Process Monitor'])}\n\n{random.choice(['Selalu gunakan VM untuk analisis.', 'Isolasi sistem yang terinfeksi.'])}"
    
    # Jawaban umum cybersecurity
    return f"{question.replace('?', '')} adalah aspek penting dalam cybersecurity. {fake.paragraph()}"

# Fungsi utama untuk membuat dataset
def generate_dataset(num_samples):
    data = []
    
    for _ in range(num_samples):
        # Tentukan apakah pertanyaan programming atau cybersecurity (60:40 ratio)
        if random.random() < 0.6:
            question = generate_programming_question()
            answer = generate_programming_answer(question)
            category = 'programming'
        else:
            question = generate_cybersecurity_question()
            answer = generate_cybersecurity_answer(question)
            category = 'cybersecurity'
        
        # Tambahkan beberapa pertanyaan khusus
        if random.random() < 0.01:  # 1% chance untuk pertanyaan khusus
            question = "siapa kamu?"
            answer = "Saya Sebuah AI yang dibuat khusus oleh SukaLebok06 untuk membantu anda tentang cybersecurity dan pentester, dapat juga membantu menyelesaikan permasalahan pada kodingan anda."
            category = 'special'
        
        data.append({
            'question': question,
            'answer': answer,
            'category': category,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return pd.DataFrame(data)

# Generate dataset
print(f"Membuat {TOTAL_DATA} data...")
dataset = generate_dataset(TOTAL_DATA)

# Simpan ke CSV
programming_data = dataset[dataset['category'] == 'programming']
cybersecurity_data = dataset[dataset['category'] == 'cybersecurity']
special_data = dataset[dataset['category'] == 'special']

programming_data.to_csv('training/dataset/programming.csv', index=False)
cybersecurity_data.to_csv('training/dataset/cybersecurity.csv', index=False)
special_data.to_csv('training/dataset/special.csv', index=False)

print("Dataset berhasil dibuat:")
print(f"- Programming: {len(programming_data)} entri")
print(f"- Cybersecurity: {len(cybersecurity_data)} entri")
print(f"- Special: {len(special_data)} entri")
print("\nFile disimpan di folder training/dataset/")