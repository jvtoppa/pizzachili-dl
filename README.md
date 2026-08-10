# How to Install:


```
git clone https://github.com/jvtoppa/pizzachili-dl.git
cd pizzachili-dl
pip install -e .
```

# Example usage:

```
pizzachili-dl -nrep -st dblp.xml -s 50MB -gz
```

Downloads a prefix of the non-repetitive dataset dblp.xml, sized 50MB and unzips the generated file right after.
For help,

```
pizzachili-dl --help
```
