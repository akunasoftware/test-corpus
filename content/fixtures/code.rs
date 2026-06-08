struct Finding {
    area: &'static str,
    severity: &'static str,
    detail: &'static str,
}

fn describe(finding: &Finding) -> String {
    format!("{} [{}]: {}", finding.area, finding.severity, finding.detail)
}

fn main() {
    let findings = [
        Finding { area: "layout", severity: "low", detail: "spacing checked" },
        Finding { area: "copy", severity: "medium", detail: "extraction fixture marker: shared code sample" },
        Finding { area: "links", severity: "low", detail: "anchors valid" },
    ];

    for finding in findings.iter() {
        println!("{}", describe(finding));
    }
}
