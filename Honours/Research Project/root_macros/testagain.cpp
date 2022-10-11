#ifdef __CLING__
#pragma cling optimize(0)
#endif
void testagain()
{
//=========Macro generated from canvas: c1/c1
//=========  (Tue Oct 11 14:38:53 2022) by ROOT version 6.26/06
   TCanvas *c1 = new TCanvas("c1", "c1",0,0,700,500);
   c1->SetHighLightColor(2);
   c1->Range(-4.26,-99313.47,-1.76,893821.2);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TH1F *MFTeta__13 = new TH1F("MFTeta__13","#eta from MFT",80,-4.01,-2.01);
   MFTeta__13->SetBinContent(0,90019);
   MFTeta__13->SetBinContent(1,5471);
   MFTeta__13->SetBinContent(2,6374);
   MFTeta__13->SetBinContent(3,7389);
   MFTeta__13->SetBinContent(4,9065);
   MFTeta__13->SetBinContent(5,11705);
   MFTeta__13->SetBinContent(6,15532);
   MFTeta__13->SetBinContent(7,20825);
   MFTeta__13->SetBinContent(8,29537);
   MFTeta__13->SetBinContent(9,41066);
   MFTeta__13->SetBinContent(10,55228);
   MFTeta__13->SetBinContent(11,72710);
   MFTeta__13->SetBinContent(12,91386);
   MFTeta__13->SetBinContent(13,114347);
   MFTeta__13->SetBinContent(14,139915);
   MFTeta__13->SetBinContent(15,167331);
   MFTeta__13->SetBinContent(16,197338);
   MFTeta__13->SetBinContent(17,227250);
   MFTeta__13->SetBinContent(18,259702);
   MFTeta__13->SetBinContent(19,292922);
   MFTeta__13->SetBinContent(20,328189);
   MFTeta__13->SetBinContent(21,363855);
   MFTeta__13->SetBinContent(22,396436);
   MFTeta__13->SetBinContent(23,429217);
   MFTeta__13->SetBinContent(24,460771);
   MFTeta__13->SetBinContent(25,489531);
   MFTeta__13->SetBinContent(26,516435);
   MFTeta__13->SetBinContent(27,539281);
   MFTeta__13->SetBinContent(28,561404);
   MFTeta__13->SetBinContent(29,575424);
   MFTeta__13->SetBinContent(30,592186);
   MFTeta__13->SetBinContent(31,604483);
   MFTeta__13->SetBinContent(32,617398);
   MFTeta__13->SetBinContent(33,625032);
   MFTeta__13->SetBinContent(34,637134);
   MFTeta__13->SetBinContent(35,647220);
   MFTeta__13->SetBinContent(36,655173);
   MFTeta__13->SetBinContent(37,667002);
   MFTeta__13->SetBinContent(38,674259);
   MFTeta__13->SetBinContent(39,683925);
   MFTeta__13->SetBinContent(40,692706);
   MFTeta__13->SetBinContent(41,697768);
   MFTeta__13->SetBinContent(42,704075);
   MFTeta__13->SetBinContent(43,710793);
   MFTeta__13->SetBinContent(44,716508);
   MFTeta__13->SetBinContent(45,721128);
   MFTeta__13->SetBinContent(46,728859);
   MFTeta__13->SetBinContent(47,732470);
   MFTeta__13->SetBinContent(48,733495);
   MFTeta__13->SetBinContent(49,738654);
   MFTeta__13->SetBinContent(50,742536);
   MFTeta__13->SetBinContent(51,746461);
   MFTeta__13->SetBinContent(52,748457);
   MFTeta__13->SetBinContent(53,751949);
   MFTeta__13->SetBinContent(54,751556);
   MFTeta__13->SetBinContent(55,755697);
   MFTeta__13->SetBinContent(56,752743);
   MFTeta__13->SetBinContent(57,751084);
   MFTeta__13->SetBinContent(58,754225);
   MFTeta__13->SetBinContent(59,755696);
   MFTeta__13->SetBinContent(60,756674);
   MFTeta__13->SetBinContent(61,755308);
   MFTeta__13->SetBinContent(62,749966);
   MFTeta__13->SetBinContent(63,735445);
   MFTeta__13->SetBinContent(64,715240);
   MFTeta__13->SetBinContent(65,684320);
   MFTeta__13->SetBinContent(66,640217);
   MFTeta__13->SetBinContent(67,586584);
   MFTeta__13->SetBinContent(68,523655);
   MFTeta__13->SetBinContent(69,457127);
   MFTeta__13->SetBinContent(70,388213);
   MFTeta__13->SetBinContent(71,321610);
   MFTeta__13->SetBinContent(72,261129);
   MFTeta__13->SetBinContent(73,209277);
   MFTeta__13->SetBinContent(74,164151);
   MFTeta__13->SetBinContent(75,128744);
   MFTeta__13->SetBinContent(76,100537);
   MFTeta__13->SetBinContent(77,79155);
   MFTeta__13->SetBinContent(78,62519);
   MFTeta__13->SetBinContent(79,50911);
   MFTeta__13->SetBinContent(80,43111);
   MFTeta__13->SetBinContent(81,470109);
   MFTeta__13->SetEntries(3.649033e+07);
   MFTeta__13->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   MFTeta__13->SetLineColor(ci);
   MFTeta__13->GetXaxis()->SetTitle("#eta");
   MFTeta__13->GetXaxis()->SetLabelFont(42);
   MFTeta__13->GetXaxis()->SetTitleSize(0.05);
   MFTeta__13->GetXaxis()->SetTitleOffset(0.7);
   MFTeta__13->GetXaxis()->SetTitleFont(42);
   MFTeta__13->GetYaxis()->SetTitle("Counts");
   MFTeta__13->GetYaxis()->SetLabelFont(42);
   MFTeta__13->GetYaxis()->SetTitleSize(0.05);
   MFTeta__13->GetYaxis()->SetTitleOffset(0.75);
   MFTeta__13->GetYaxis()->SetTitleFont(42);
   MFTeta__13->GetZaxis()->SetLabelFont(42);
   MFTeta__13->GetZaxis()->SetTitleOffset(1);
   MFTeta__13->GetZaxis()->SetTitleFont(42);
   MFTeta__13->Draw("");
   
   TPaveText *pt = new TPaveText(0.3988983,0.9339831,0.6011017,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("#eta from MFT");
   pt->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
