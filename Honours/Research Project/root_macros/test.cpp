void test() {
    TFile* fr = new TFile("AnalysisResults_pass4_full_weird.root", "READ");

    HistogramRegistry* histReg;
    fr->GetObject("fwd-registry", HistogramRegistry);
    // eta->Draw();
}