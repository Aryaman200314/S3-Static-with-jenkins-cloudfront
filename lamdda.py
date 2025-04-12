import boto3

def lambda_handler(event, context):
    cloudfront = boto3.client('cloudfront')
    distribution_id = os.environ['E2E15LSKGLP2O2']
    response = cloudfront.create_invalidation(
        DistributionId=distribution_id,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': ['/*']  
            },
            'CallerReference': str(time.time())
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Invalidation created successfully!')
    }
