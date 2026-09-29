# Failure Analysis and Deployment Handoff

## Failure Analysis Exercise

The automated test suite is the first failure-detection point. When a test
fails, capture:

1. Test ID and scenario name
2. Input values
3. Expected command
4. Actual command or exception
5. Suspected decision-rule defect
6. Corrective change and rerun result

### Example

If the threshold comparison changes from `<=` to `<`, scenario B01 fails:

```text
B01 | FAIL | expected=ON | actual=OFF
```

The failure shows that the defined threshold is inclusive. Restore the
inclusive comparison and rerun both the unit suite and CSV scenario runner.

## Local Execution

```text
python -m unittest discover -s tests -v
python -m scripts.run_aeb_scenarios --report reports/aeb-scenario-report.txt
```

## AWS Deployment Handoff

AWS deployment is outside the local MVP implementation and requires an AWS
account, credentials, region, and a selected hosting target. No credentials
are stored in this repository.

The generated report can be deployed to an approved AWS target such as an S3
bucket:

```text
aws s3 cp reports/aeb-scenario-report.txt s3://<approved-bucket>/aeb-scenario-report.txt
```

Before execution, configure AWS authentication through the standard AWS CLI
credential mechanism and obtain approval for the target bucket. The CI job
currently validates the software and scenario runner; adding deployment
requires protected repository secrets and an explicit AWS environment.