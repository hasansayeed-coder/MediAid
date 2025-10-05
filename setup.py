
from setuptools import setup, find_packages

setup(
    name='MediGenius',
    version='1.0.0',
    author='Hasan Sayeed',
    author_email='hasansayeed791@gmail.com',
    description='Industry-grade Medical AI Assistant using LangGraph, RAG, and Wikipedia fallback.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Md-Emon-Hasan/MediGenius',
    # packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'huggingface-hub',
        'langchain-core',
        'langchain-community',
        'langchain_huggingface',
        'langchain-groq',
        'langgraph',
        'python-dotenv',
        'sentence-transformers',
        'pypdf',
        'pytest',
        'torch',
        'tensorflow',
        'langchain-chroma',
        'transformers',
        'wikipedia',
        'duckduckgo-search',
        'chromadb',
        'python-jose',
        'passlib',
        'gunicorn',
        'flask',
        'pytest'
    ],
    python_requires='>=3.9',
    classifiers=[
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'medical-ai-app=app:main',
        ],
    },
)