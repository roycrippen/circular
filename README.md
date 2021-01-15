# circular dependencies

Utility to find circular dependencies in Java classes. <br><br>
Defaults to a search max depth of 5 (a->b->c->d->e->a). <br>
Change call entities.find_circular_deps(level=5) in main.py for alternative. <br><br>
By default system classes are excluded that start with: <br>
excludes = ['java.', 'javax.', 'sun.', 'jdk.', 'com.sun'] <br>
Add or remove items from this list in entities.py, function read_dep_file.

## requires 

* [jdeps](https://docs.oracle.com/javase/9/tools/jdeps.htm#JSWOR690)
* [python3](https://www.python.org/downloads/)

## create txt dependency file

``` 
# create dependency text file
$ jdeps -R -v some/path/your.jar > your.jar.txt

# examaple
$ jdeps -R -v jenetics-6.1.0.jar > jenetics-6.1.0.jar.txt 
```

## run examples

python3 main.py jar package1 package2...

```
# all non-system packages
$ python3 main.py java/circular_test/circular_test-1.0-SNAPSHOT.jar.txt 

# or
$ python3 main.py jenetics-6.1.0.jar.txt

# one package 
$ python3 main.py jenetics-6.1.0.jar.txt io.jenetics.util

# two packages 
$ python3 main.py jenetics-6.1.0.jar.txt io.jenetics.util io.jenetics.internal
```    

    
