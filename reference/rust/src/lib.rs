use serde_json::Value;
use url::Url;

#[derive(Debug, PartialEq)]
pub enum SspError {
    RequiredField,
    UnsupportedVersion,
    InvalidUri,
    InvalidAddress,
    InvalidEntity,
    InvalidTransition,
    InvalidPayload,
    InvalidProvenance,
    InvalidExtensions,
}

pub fn validate_packet(v: &Value) -> Result<(), SspError> {
    let o = v.as_object().ok_or(SspError::RequiredField)?;
    for k in ["ssp","id","profile","semantic_address","action","subject","reach","provenance","extensions"] {
        if !o.contains_key(k) { return Err(SspError::RequiredField); }
    }
    if o.get("ssp").and_then(Value::as_str) != Some("1.0-draft") {
        return Err(SspError::UnsupportedVersion);
    }
    for k in ["id","profile"] {
        let s = o.get(k).and_then(Value::as_str).ok_or(SspError::InvalidUri)?;
        Url::parse(s).map_err(|_| SspError::InvalidUri)?;
    }
    let a = o.get("semantic_address").and_then(Value::as_object).ok_or(SspError::InvalidAddress)?;
    if a.get("space").and_then(Value::as_str).unwrap_or("").is_empty() { return Err(SspError::InvalidAddress); }
    if a.get("coordinates").and_then(Value::as_array).map(|x| x.is_empty()).unwrap_or(true) { return Err(SspError::InvalidAddress); }
    if !o.get("extensions").map(Value::is_object).unwrap_or(false) { return Err(SspError::InvalidExtensions); }
    Ok(())
}
