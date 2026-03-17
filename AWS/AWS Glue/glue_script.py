import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1773419749287 = glueContext.create_dynamic_frame.from_catalog(database="cleaned-youtube-database-27", table_name="cleaned_statistics_reference_data", transformation_ctx="AWSGlueDataCatalog_node1773419749287")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1773419877485 = glueContext.create_dynamic_frame.from_catalog(database="cleaned-youtube-database-27", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1773419877485")

# Script generated for node Join
Join_node1773419895536 = Join.apply(frame1=AWSGlueDataCatalog_node1773419749287, frame2=AWSGlueDataCatalog_node1773419877485, keys1=["id"], keys2=["category_id"], transformation_ctx="Join_node1773419895536")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=Join_node1773419895536, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1773419744567", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1773420049902 = glueContext.getSink(path="s3://youtube-analytics-bucket-27", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region", "category_id"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1773420049902")
AmazonS3_node1773420049902.setCatalogInfo(catalogDatabase="db_youtube_analytics",catalogTableName="final-anaytics-youtube-27")
AmazonS3_node1773420049902.setFormat("glueparquet", compression="snappy")
AmazonS3_node1773420049902.writeFrame(Join_node1773419895536)
job.commit()