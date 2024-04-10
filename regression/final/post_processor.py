from opentelemetry import trace
from opentelemetry.sdk.trace import TraceProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
import subprocess

exporter = OTLPSpanExporter(
        endpoint = "202.83.19.71",
        insecure = True,
        )

tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)
span_processor = BatchSpanProcessor(exporter)
tracer_provider.add_span_processor(span_processor)

regress_file = 'regress.scr'

with open(regress_file, 'r')as file:
    for line in file:
        subprocess.run(line, shell=True)


span_processor.shutdown()
