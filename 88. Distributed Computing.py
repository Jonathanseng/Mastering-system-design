# ython code for distributed computing using the PySpark library, which is a Python interface to Apache Spark:

from pyspark import SparkContext, SparkConf

# Define a function to be executed in parallel
def square(x):
    return x * x

if __name__ == "__main__":
    # Create a Spark context with a local cluster
    conf = SparkConf().setAppName("Distributed Computing").setMaster("local[2]")
    sc = SparkContext(conf=conf)

    # Create an RDD (Resilient Distributed Dataset) with some data
    data = sc.parallelize(range(1, 1000))

    # Apply the square function to the RDD using the map() transformation
    squares = data.map(square)

    # Collect the results back to the driver program
    results = squares.collect()

    # Print the first 10 results
    print(results[:10])

    # Stop the Spark context
    sc.stop()


# In this example, we define a function square() that takes a number and returns its square. We then create a Spark context with a local cluster of two worker nodes, and create an RDD with some data (the numbers from 1 to 999). We apply the square() function to the RDD using the map() transformation, which applies the function to each element of the RDD in parallel. Finally, we collect the results back to the driver program (the program that submitted the Spark job) using the collect() action, and print the first 10 results. Finally, we stop the Spark context to release the resources.
