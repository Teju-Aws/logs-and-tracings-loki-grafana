from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
import time

# Configure tracer provider
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Configure OTLP HTTP exporter
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")

# Add span processor
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

# Send test span
with tracer.start_as_current_span("test-span"):
    print("✅ Sending test trace...")
    time.sleep(1)
