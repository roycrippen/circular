# circular_test

Test Java application with intentional circular dependencies.

## requires

* [jdeps](https://docs.oracle.com/javase/9/tools/jdeps.htm#JSWOR690)
* [maven](https://maven.apache.org/)

## create txt dependency file

``` 
# from root application directory

# build application jar
$ mvn clean install

# get dependencies
$ jdeps -R -v target/circular_test-1.0-SNAPSHOT.jar > circular_test-1.0-SNAPSHOT.jar.txt
```
