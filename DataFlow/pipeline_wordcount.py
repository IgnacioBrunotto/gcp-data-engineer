import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run(): 
    #config del pipeline
    options = PipelineOptions(
        runner= "DataflowRunner", #cmbiar 
        project = "gcp-data-engineer-498722",
        region = "us-central1",
        temp_location=  "gs://gcs-bucket-curso-041/temp"
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            |"leer archivo" >> beam.io.ReadFromText("gs://dataflow-samples/shakespeare/kinglear.txt")
            |"separar palabras" >> beam.FlatMap(lambda line: line.split())
            |"Contar palabras" >> beam.combiners.Count.PerElement()
            |"Guardar resultados" >> beam.io.WriteToText("gs://gcs-bucket-curso-041/output/wordcount")

        )

if __name__ == "__main__":
    run()