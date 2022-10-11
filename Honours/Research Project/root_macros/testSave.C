#ifdef __CLING__
#pragma cling optimize(0)
#endif
void testSave()
{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Tue Oct 11 17:45:11 2022) by ROOT version 6.26/06
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",380,79,1361,853);
   Canvas_1->Range(-4.26,-76694.11,-1.76,690246.9);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameBorderMode(0);
   
   TH1F *MFTeta__2 = new TH1F("MFTeta__2","#eta_{MFT}",80,-4.01,-2.01);
   MFTeta__2->SetBinContent(0,87);
   MFTeta__2->SetBinContent(1,47);
   MFTeta__2->SetBinContent(2,87);
   MFTeta__2->SetBinContent(3,174);
   MFTeta__2->SetBinContent(4,404);
   MFTeta__2->SetBinContent(5,878);
   MFTeta__2->SetBinContent(6,2029);
   MFTeta__2->SetBinContent(7,4301);
   MFTeta__2->SetBinContent(8,8276);
   MFTeta__2->SetBinContent(9,14988);
   MFTeta__2->SetBinContent(10,24854);
   MFTeta__2->SetBinContent(11,39210);
   MFTeta__2->SetBinContent(12,57258);
   MFTeta__2->SetBinContent(13,79341);
   MFTeta__2->SetBinContent(14,105310);
   MFTeta__2->SetBinContent(15,134398);
   MFTeta__2->SetBinContent(16,165141);
   MFTeta__2->SetBinContent(17,197054);
   MFTeta__2->SetBinContent(18,228938);
   MFTeta__2->SetBinContent(19,261426);
   MFTeta__2->SetBinContent(20,297994);
   MFTeta__2->SetBinContent(21,336274);
   MFTeta__2->SetBinContent(22,368629);
   MFTeta__2->SetBinContent(23,399487);
   MFTeta__2->SetBinContent(24,424210);
   MFTeta__2->SetBinContent(25,449154);
   MFTeta__2->SetBinContent(26,478213);
   MFTeta__2->SetBinContent(27,502816);
   MFTeta__2->SetBinContent(28,524339);
   MFTeta__2->SetBinContent(29,536572);
   MFTeta__2->SetBinContent(30,550460);
   MFTeta__2->SetBinContent(31,564165);
   MFTeta__2->SetBinContent(32,562415);
   MFTeta__2->SetBinContent(33,567491);
   MFTeta__2->SetBinContent(34,563145);
   MFTeta__2->SetBinContent(35,567877);
   MFTeta__2->SetBinContent(36,564528);
   MFTeta__2->SetBinContent(37,563183);
   MFTeta__2->SetBinContent(38,564654);
   MFTeta__2->SetBinContent(39,577428);
   MFTeta__2->SetBinContent(40,575604);
   MFTeta__2->SetBinContent(41,584336);
   MFTeta__2->SetBinContent(42,581156);
   MFTeta__2->SetBinContent(43,582526);
   MFTeta__2->SetBinContent(44,570740);
   MFTeta__2->SetBinContent(45,563569);
   MFTeta__2->SetBinContent(46,563797);
   MFTeta__2->SetBinContent(47,564981);
   MFTeta__2->SetBinContent(48,563414);
   MFTeta__2->SetBinContent(49,553329);
   MFTeta__2->SetBinContent(50,538577);
   MFTeta__2->SetBinContent(51,531181);
   MFTeta__2->SetBinContent(52,515045);
   MFTeta__2->SetBinContent(53,503066);
   MFTeta__2->SetBinContent(54,501152);
   MFTeta__2->SetBinContent(55,495563);
   MFTeta__2->SetBinContent(56,485831);
   MFTeta__2->SetBinContent(57,459302);
   MFTeta__2->SetBinContent(58,449278);
   MFTeta__2->SetBinContent(59,443680);
   MFTeta__2->SetBinContent(60,433769);
   MFTeta__2->SetBinContent(61,429212);
   MFTeta__2->SetBinContent(62,410422);
   MFTeta__2->SetBinContent(63,402863);
   MFTeta__2->SetBinContent(64,401885);
   MFTeta__2->SetBinContent(65,394105);
   MFTeta__2->SetBinContent(66,386451);
   MFTeta__2->SetBinContent(67,357759);
   MFTeta__2->SetBinContent(68,312853);
   MFTeta__2->SetBinContent(69,256275);
   MFTeta__2->SetBinContent(70,195075);
   MFTeta__2->SetBinContent(71,131304);
   MFTeta__2->SetBinContent(72,82932);
   MFTeta__2->SetBinContent(73,45773);
   MFTeta__2->SetBinContent(74,25110);
   MFTeta__2->SetBinContent(75,9807);
   MFTeta__2->SetBinContent(76,2944);
   MFTeta__2->SetBinContent(77,805);
   MFTeta__2->SetBinContent(78,119);
   MFTeta__2->SetBinContent(79,20);
   MFTeta__2->SetBinContent(80,12);
   MFTeta__2->SetBinContent(81,18);
   MFTeta__2->SetEntries(2.619288e+07);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *ptstats_LaTex = ptstats->AddText("MFTeta");
   ptstats_LaTex->SetTextSize(0.0368);
   ptstats_LaTex = ptstats->AddText("Entries =   2.619288e+07");
   ptstats_LaTex = ptstats->AddText("Mean  = -2.951");
   ptstats_LaTex = ptstats->AddText("Std Dev   = 0.3688");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   MFTeta__2->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(MFTeta__2);
   MFTeta__2->SetFillColor(2);
   MFTeta__2->SetFillStyle(3006);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   MFTeta__2->SetLineColor(ci);
   MFTeta__2->GetXaxis()->SetTitle("#eta_{mft}");
   MFTeta__2->GetXaxis()->SetLabelFont(42);
   MFTeta__2->GetXaxis()->SetTitleOffset(1);
   MFTeta__2->GetXaxis()->SetTitleFont(42);
   MFTeta__2->GetYaxis()->SetLabelFont(42);
   MFTeta__2->GetYaxis()->SetTitleFont(42);
   MFTeta__2->GetZaxis()->SetLabelFont(42);
   MFTeta__2->GetZaxis()->SetTitleOffset(1);
   MFTeta__2->GetZaxis()->SetTitleFont(42);
   MFTeta__2->Draw("");
   
   TPaveText *pt = new TPaveText(0.4626206,0.9301351,0.5373794,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("#eta_{MFT}");
   pt->Draw();
   
   TLegend *leg = new TLegend(0.1245111,0.626322,0.4243807,0.8354877,NULL,"brNDC");
   leg->SetBorderSize(1);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("MFTeta","#eta_{MFT}","lpf");
   entry->SetFillColor(2);
   entry->SetFillStyle(3006);

   ci = TColor::GetColor("#000099");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(1);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   Canvas_1->Modified();
   Canvas_1->cd();
   Canvas_1->SetSelected(Canvas_1);
}
