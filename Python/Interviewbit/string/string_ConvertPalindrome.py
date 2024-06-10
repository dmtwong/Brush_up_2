# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:47:56 2024

@author: USER
"""

# Problem Description

# Given a string A consisting only of lowercase characters, we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.

# If it is possible then return 1 else return 0.

# Problem Constraints
# 3 <= |A| <= 105
#  A[i] is always a lowercase character.

# Input Format
# First and only argument is an string A.

# Output Format
# Return 1 if it is possible to convert A to palindrome by removing exactly one character else return 0.

# Example Input
# Input 1:

  A = "abcba"
# Input 2:

  A = "abecbea"
solve(A)
# Example Output
# Output 1:

#  1
# Output 2:

#  0

# Example Explanation
# Explanation 1:

#  We can remove character ‘c’ to make string palindrome
# Explanation 2:

#  It is not possible to make this string palindrome just by removing one character 
# class Solution:
    # @param A : string
    # @return an integer
def solve(A):
    dict_Palindrome = {}
    n_A = len(A)
    # list_A = list(A)
    # isOdd = bool(n_A % 2)
    n_comp = n_A // 2
    for i in range(n_A):
        ifPar = True 
        # copy_A = list_A[:]
        # print(copy_A, i)
        # copy_A.pop(i)
        ix_cur = [j for j in range(n_A) if j != i]
        # print(ix_cur)
        # print(i, copy_A)      
        cur_keys = []
        # print('here',
        for k in range(n_comp):
            cur_keys.append( (ix_cur[k], ix_cur[-(k+1)]) )
        # print(cur_keys)
        for cur_key in cur_keys:
            isPar = True
            try: 
                if dict_Palindrome[cur_key] == False:
                    isPar = False
                    # print(cur_key, isPar)
                    break
                else:
                    # print(cur_key, isPar)
                    continue
            except:
                ix_1, ix_2 = cur_key
                result = bool(A[ix_1] == A[ix_2])
                # print(A[ix_1], A[ix_2], result)
                # print()
                dict_Palindrome[cur_key] = result
                if result == False:
                    isPar = False
                    # print(cur_key, isPar)
                    break
                else:
                    # print(cur_key, isPar)
                    continue
        # print(i, isPar, dict_Palindrome)
        if isPar == True:
            return 1
    return 0


A1 = 'yxhjxsvubfwqabskydqpojhllbhfwpelphpqauqhrfgglygbsethloffnqbmcpiiykwpjkiibzbijegfegzbbbqlsvxbvqkffkbdvcqagvjdcfgpouhqfecenffbrovozlupwxxpngskdvxrbidwaifoczzcjnbalififxemhgawclznhxzayrhbibsechibdrylhurjmfrblyikaxcsohdvzgamqjfkixnbkoggwmcjoenvyinfpzifkafxxroaptlbvnrcvhwxgyzggekirqensvslajltetwjnqxkrgzlyymmptxkpctjvjlggjngkpswiahhofnelizlohkigomjqkqxcrbvmlrzjbjyouhzdarvbaxpuatkcosalnahspmbluhzzkhvombgcmoegpuwbnvwvnksdekpqdtqjflbvphdivbjijuxvymlevhhqatkwkkalgylvzywagjvvjhxkhlhbstxxexjgvfdajairncsetfruwftqoktdmonzeatribmnnogfwvvnmearehpxnouwlzkuraxyrxwccsdzsieatgtputwvkforvcjdboxpnyoxayexjrkjylbyksuapsjtwxtprtufubdtpvcjteghryphdieogxgmsamybnbhjdzvctfleatvyqajvxjbkyptnqzfwcxlprbizuhouduryytiykgnkonhuzpuqnhoolfavdvbvfegxegjobaaqdnaerxuisuewtxnvmqdmzpyjgyrtqqxjfmbftigqddiwnabrdskdtwgceuixwjpnarymcngmvcubydcnhydyilnygrrilrtaxuwtqthogkbndxybnagxqkfhzylbfndcbmsebccanxwzejvrnkumhndfahgybevgqnavcndnapbjrhpareqfaybkwvzrkjygikjnbppsbzltobyjxumwtqewkqwiqlxpejxemrfrlmdzyqtalprqqcxycrmnjhuzkxjxndvpccsbyereztdluvduyucivicfetwgfnpuzpgdhshttzrmgtycgqyhuggfpevypncuoejduvpfxqwaabyqngrkiwcbthilhlllzbedcaxsvuubyehayrnvdgliegvttexpndqaiqoaxjenorvypafvdlupvwnhvcpiwtfcdhnfivbtgduyufgcwhhmlsvomednwogwoknsrkluzxtbkjcysvvmwjqsbxjkjjwzvredslfasqpjbuqhckxtiwqeeiguipbuujgnniiurefetghrpejlfgwqxcraensefyldzcyiqwfeqqzjfwdaxizekiwatzmxbjlnmnlqhjnzxnncikumpnrazdekryfkjpirsxswhkcvnrmutrnhyciyftekqkaghsosnzcinmfqggauuthbizzkzhuqrnkzrjllmewsncvgyxmytnyufltclvjftybcxcnsicayjlovdpgememkffhczyvhuihhysvyvdftbxdgwkkykcngxsbtwmpqolvkbfwffkcfwrlvhhuuywqcmbdjkdorfxguvcbfcljzsxgswnjcsqdwkljdrtueyljlpmwgnttwzivxqvjsilaizlruwnqnfbsquilijpeauwgcoomzyxyipbbspldgaendjfzboivfkovpgypxxlvgrofxvtpkyystnnpjchzgvvjawztdiumwvshcepmfopjctfoctfcsdfoqdcwkdvunrqtkagepajgavlgdazevvvspltjmwjffqeehcjklswvrbaryhtckxzjvajdtztsofwzeuhwninsfbwzzwkvnzywkmpyqvgkwsylzidsbjzntqmaiygyszuawwydseqirdvimvrbtklgyhzkbtjkxqwnxzdtbeeefhdgfnjibgtbqspteysvocjypbdcoansqkqswqghamcksxvnjjenhzsiimdiddkbuugzpfmkxovugcbcxcfdmvgvkyxmqpmquvayjueouwfacsgrcebsiyvymqgzziynaiyvouheyjrhyhopuhznljwvmonwgyhxnyapltalpqrbobilfwrgqlhrisxqpdcnszovjfmwhfioojvnfxmxovkhmenrkjrfnpzluvhhowwhjaodoqnqvlmfoyslmazuyibuclgggwxvvgwakwxzltgayhhltystgtzchmlidpsahrrtvlxmrmdfegbmhbcghartrkfiafsvyiutvhkcyaqipkaqqtmwgfsiptkxxnybqdvzvlbigxzzhrrwetfsjhdhxuznnhpkxodvtsonasqbgbsfzidatfpuxjzefvdjobmzojqdkfswusfptupamdhrqwoupimzghdofqcputvoxdpnxfphqxqfuyaxzczkxxtfxplrqsknvrrwosqapmnntysffkqbklkkleqgoyoqusjmwzcebgynpjcixmucfbtvlxwjqynfquwzyggqrjcubzfuocyawliryvweuebpfdeoktparbuffeqrypfqjygibkjgixhbakqeaxfoizjarqwyxtokyefwwwurvntitkkialyzfoiewxgqdappnhsdcdzsdmyygjftcrbmmiexgmjashfioswybqdccpvjtfgfdnmbrpeofeiuapwdhuqcjxfvoqbgsscmbvotwjqingwarkhwtpxrbuespfjijiklzyannlnxutftzgafuxthpabaznmykyedwhhrrtfytduiotwwrpdugihfcwxmiptcimwpsxykfqyvzpuxpjfheqrazodbtbpvhjqixijpqogrkhkelhciyoloyawsdwyvjkwxqgfptydhikbpwxcdwduvhwpnapxosinjmeirwzykqyvcmkihenjjopkgmsnzxnbtrfayjhouajnagxxruinptltshpsfidtvmeabmolxydjyfmlvwvriykrqnfeectwhhfmlfneetxentltjroortvtxeossrsvqrqlkkuzmksprnanoupbdwqffzsumcezxspvcrxsorszntqksxhbmnjpmeepzrrnpneggdkwgllbfbvwrfivqjtieafrwcvoccbihyyktyphqzvqvgobsmvccmpkiqsbgferxwokvcncpczhlemchwiabakbjfsqxkhujzocdlvsicuyevdbvdrfsoodfapgttkcqrkbstbcsocaqhhtzzlgufiaphnhckkcqqgrwegoxnftyjcjegrkpaowavuhrjikcwlxufglgbwgzzwwkesqjviqguspldjxxiyfsueowwpfngonvavzgzpgoocgvmlqdvklfstqtygnfvkkeeopoetrrqvkbyoqtlmteqkgmxxslgowxerdesfannxckpdilxlrxmpqikpjqfjcaagybfpixdsgincyytwyzyotvghldexftowdtplucpjdeczppladrnbyblnkktzwdkmdrugpwhgllqffctuuhcmgpktveiwgkyydiquanipblvpnokqemfdevrtidvruhkyikiibycqwbqtnhuqznjwnpyuiwhkdjmoboggrkqkfxfhywwjzkquejjenacivbbrhkxqruxsbanrpwjvnduskkyjsvqkxxzfujsjmtvmoplbrnluwtfqgclwsaxkrltypszbzdrijibktolrexxmsmlqmufcjxqppvumbqrkdwfbduwocigbxpybffwlqbpdplsbjfstpwigmhhimjmfqedpjyklfplwqfsuxvguwibtnqtpgkxycxjdvikneroogxchsctttzohjwelhvcpgwstvrahyfjboxrzolzodtcyfpfpftnsrfctuubpllkzeyrcqtizzvhoooitufbdcgftifsywiaqtdofmmejwclstsdvkhffhfzgyfzkpdvyjpuubpfmqkcmjdkyeerkzlrjjzihfnkzzbdfiukmwkeyvlzyoxhfbvtextcffigxmzhlrezgnpdzpvovxysykkdzjmwhqqfqhvimnkynizehkozwluypzkxittsajssclkxrqgbjisjfvvezfoqrdxxskuncqppncfqipdysigdzlwypwkckxevpmpnvafxizschiuhevzxdxztohexuaylpqdgtvjawkmyzchsdclhswuacfbpoterrvrwjeyxmgyywyvdrscrwldqwyosgozzawgfavszahiaeplkwlazskclszokukhoemdbnnkliknhmeheowdnigfzjsfenygstfiuhfjolesmifotjopusfwlhmmsgvfyuenujdzolzdluxylzowrrghnklwlpwhfftlmcotiwcjdnxcednosnbpapyhccmmgmntsfwixpzhqmmbwuzuaoajasiizggrgtqdgzmwputnoxalrwznrfdawvspbnkfpzjswkwbrsapfgbjvdtylkjewhnjznfomvrvgwnezvxonfztlkopajepsrrfqgrmkvioewsedpdpamiuhzkkdveqgyhlnvyoplhawkaagfhlgyljlegaiybkmucjoerdoluqtcmbulwyccgkpdpqyhkynprqwfvmzcymptmfeggeykkmvzuoxwtyptfgfioasktamxlwwaidpgjmjlmtctwpdcrvrtuhjdktcfnjfnxtmvzsxnlervpyaoatarollcicltzlfgauxdrkzlklwanlelrjolglcyeovzbiohfgqgcqojypssoxddjszwpabtdqwwkpmyalgpmnsaepiatstaqcfucwfhzumkblpdbdilnnadulmvwcwehronyuulzofbmkmzwcwfympiuwnnqehvrdpkktihzdyykvxhqybfxfnlwvtmgwazhmuzbprdcktvjullrvbrvpwiskeoxefrioauajppyndiacmjeeszzkbyhhajguecblcerwpmilnqpexgxkmbgohtjxpootpebvdxluyzjrpyduqiyxtdjosfxzjyocshugmmececzvlajtdxkghbhsdfdgotsfxmnmpxdtevzmaokwjacucvvcoexuqzlvyjupleyraktfqmlpipijfxdkledbjzirdotvzkhyoyyyeisunmymwmslsljfgrodgvhpxxuvuharymuzikjpsldgthkhffesofjckgibwrirdmzoouhxifbhukflaavsztznkpjhalnxfwtftzvpoovqnorvhogcljlibkuftcikaqlsrkcvgjmvbvwyszhvmhqtfimodmwtrwqpuajwxsnxqblwmyblqxybjjljxprqettuoenngfmskexymecbcyijnrdayuotievxavxsteeanwrniwmovjyimcdisznlthuatqwztsxujosxlnkildgkhzcxlidleuyxhdwpqiarsngxrojzfhtpojcippgblyujbcyvsthrgjgcccbqpasnzmbxolvcgbuldxtyxejwawkbuoqodhdicoqxvnlxtxjiznknngnpfdfqdzjoxjgcxhnpijwweywsnvqeclfqxebtdtmxbdybwcthvdlmilmvfbafmnkfppfbcaqbhjxvfoligfacidycyxthgusgfgetjadakvactzurpgkwiuikatujkneafohdkanrgcedgtzjawperyjvqeuldggkdyfwwvezymqrmaaqnfcxlxoalcfwwlrajkcfgrgcrtjzvjmqeksnykuadpszfdauumpujukdbkfdhwlixcskeyheiuomghncyazqigffybtlwfbdljrmjlvwaowkqvstibbspuscokpawhbjgzzowpiulpzuopsnfavanszjjognfbsfhvxcteotejuiainyxvhhvqtjwkaseznglhrjpsscyqcvxkqdisvmnzfsbqciftxaftaehmpqlcpirjmqsldjoogvbyrcgbmoytgtvffbizufefayhbugotvywwjczvqjgmerslbwthmywxlyoygytuyyfpjvqvolktfdzaxtssyqviumpyemrwoiqplsvhkbnyrbjhvizcdcdskdxychenvqwoyvsltwfrystkppercturccokocttovhbcjytwmfofrfvzvacmbfjqyppczmqhjykytdpkpjiiwifiazmfooxfxaoicupphnqvnwgmerfeyyyeecjyswzbpvezguhlkrpoevreqhtkdzlwamjjraxopzxswscekifqmfapgehhepatvjdrzwmhostckakxwkdycmbzkqiiqghhjfhywyplbfeftodkllnjbftzmyswnkrizmplcbiaskjqsiwerpurjmenyvlmwdasugubhyhgncvibnturcktvaciizwsheirkggeitbswbrgsjwvqipebpavguxdfvwwslfbudgixtrdwhmaqcypyqsmaosjhtvjrpowoewlewadsnosqcpjjjumkztgphmnlxbioubcxmkhdciabsapqwdjeqhbepjmcjttbzqsmqffamwbvwmsihbueijbbryuvvigzzimxwocpsgukirqkivvkddsailqrnqgqsdfzwdausjldwbmulzlusdgejsjfxeyaahgjlwowfehtwdrnwznbzbaoymptnkfkcanehzfklwbrkocekwuuqokqefszkztkihbkdnabtkehdcftvaxkfgbfltfhaflsghhfoxyrfqtrjnuyfxblyhwzlugojgbrefqigvdadqzjrdjkyuajzcoperiydptqoqjgadgapkdzkgsekajnpkuaqqcjpigpirhswjxplavdrgwppkyykfdetvvqebfzodlepoyvjpanjvlktjfihzyoljyjhslllxdublyjnqmzytehxibmppgqgpulpujboacusqqoowirpgkqnqjjsdfrbdgloszfngkeqrslurcuhqsomkmdypouqxepbozaddggfawafpqlgyfcjxbfhxgyditwegzfoogefarslnexjtwawdosrwuxywzvjhypyrycotzfaelgspyvnwsarrprvlyvixixjogorbjqmblunwnwaycsdigdkbxsdczfncrvadbajiyauzgztqfkhnqwlldosxzbvjxkhlpdvhuxkwhrtzkdncldnmaqvgzoxbkgyqwkzkcgftdqqnywboyeommhzhvnsrtnxrvhnlxrauknrkyxfjyatveeclykxoefgfwpwcaubaireadzldmwkhkzbdamisyfvghbtpqxtufsilstjfnkqlfalaeexpuwaorfkdtnukmlzuxxjaeyyyalggfscvutxfcwxflhyaxtaspdkemdsgiuczahtiquvknntnpyocouvpdhapaibnihyjwuhvhzmidqvbvrfzdevfefuapvjjpfxistlxpkcurmtiawhjjlmtnvzrpbqdebzvpdzcvfzmmdqqnfrktwdhpviafzfjjencrloeigjzagypjypymhcdzpifysanpslxhhemdlchsqdibnfdlitephtfboryzkbybxtajmsmmfpbixlyaqgiqakjfzacssnwfixavbarfossdfhgtcpgfxevlbzkbddoitwpshcozgeasjzavszurtxduurwxchwdnnfrnsjhdqlafviiknumqmzmagmztxoaoqlqewqcpqoulpodflfenfagmtjihiibgsbqgqmrwvtbegrbkwdpkqwdritjmabvxwtupgirwusacurlsejrabrqaqfihyjelucvyucghhiujuygktflqxoezjhadpijiykicskttofaspzgwhhhqkwkavzkglrbowjmmjkcwzsqipuuuukydphxsyidngkzlimqwdvdikjzpmzcxocxbjzimrygnnkwtxjtczkdfeqtcptzoohjpydkfmrukvwfvcqgsybdbqymwlplwgtpkwdhjgyqnapxmxcpkmiviezfvmfjdxxeqhjaowmqjhxwjdhfuzjxbbpzttzofssfqjjyiiiryssrqgcbsonipxbypodaetmcpfawdexkclilakraqseejylukrufkergfutnhsomguvdhrkdupwcbkvgxymabrdviiiekaoiffrixlgctsuiluccdbvrhstntiragbijcyctslnysjssqoybcemlmoqviokdxutmttltdhynyshdjvabyqrjwxombwgkgndwzvvdiqlapzegcrgkstfuwrdeqgliolemhkcctdotbgitqfeinmefjuzrcwnymuiinrowzgaxvtdykbvvtootemnmbqnfqsmlopwydhzxgchkoxrshbyzdphnizooijsyweyvlarmpwyxhsnsurwmuznzmbosxviguigsczjtcnxssjlseutiskywkxlgaooibzvmzxnolpbarmlqmsbkcqzyysgzkpkrrjlpqnhusongboijzcihvtgxaixhhonimjyohhyrjmzjjlsyjuvqdmrnipgrveirvbfpfeerglkwdppsobsuqtjbgrjqkscjnzslzecbgdkexuletttwgyesyqxnykvpzvmaoxqiohbpycbuelxhfpqenpnfhexwatnvvhsfjkeglxclxdezvinakelvnndbarjxuotjvgtgjfyrqksbbsesmvdaqofvfjnvrhhizqsuwqlnmeapompktczkmnbvajlcfovsoepliecrbgtfpgiovzqicdwuqbkuzwdhgqvwzczwqohymbtivskvzumwwyukzahkxgvsuwupmfehqjmdinbcgewuggjuyaefosxljccklhykhwantokgjhumyvahnikgaxhkawvbgghlogawjbmouvkggdbnaebtjbvnusjbcuxtkvzsithpsapbwqogwigrmzoifzdgrxeyxptkokhkqutgekjcczzqsqfkucklgpxtcnypyjbitsihavzkkamlsqkccdebwmnmjbpctdhxvgdhqifoptyecxrdnbnhlfvvvmyidwjumxwkgdbwiruigbeyumpicoluvzdfnsvayenhnyvpbouunowjysslsnybnyfnauosrbhoapanwowdojfmaznzluonixgtaczhzkbwkcwpotgcmtjtcvvhfprpjflbjtwautfqffjcgxuyxsfpgkwnfqaqsxmiwjvugglzvwejtjueivvxpoqcabfmgjhfircpjcjknlpddbcyayogwcvxmemgkobronusshndimmoyanbnpbxnaynqshxqusdtxtiqzhlwqwbafyudoxyjtgxpfjqmhobrzxcacxqgrfhlueclkwrnadcclbwdpiwyaxzemwdjflbvjpasjiztujnxuzfcgnujsguuxdsrqtdasnpwqjqqquyeqzoycdufqmovvnmneifubviinwfpobwljnxuxwegvxeqieaitybddiaxtqzmtynahoqolmhnrodgujgkpnbohxgjmezwsnwfjwmmdnyvozdhywtqpkwijcqzmeewjtptcxpnzqxmmsboitxhnlaqqfvuvpbslpcxwwxeqgrjtvsizfvpxkekceocnjtqkpjckuojdfmlpztjmqzwajgybloahgwfqfbgqlpdaljqqvtkkcwrvxwvlsadjjnynsyngjyzxqqhthdvebjjvzxsvzeplkvetoywulcxrfizslqkkclxdtcwzuftqprcrvlcpddglbgktbkgnydyzhnyetdzqeqqdvkobngplepuokgdhtvsjhwomezkwozkudqadnqqcyoyzeddjryrmikssfnlxmbbfowwykyrmnllqtgkxkgugazdwsembgsowyjqordthunshactwhkcutoucqnanmfvhpzyacqnpnerpgorovixrykryablhyehwfacfbnkakxfunxoyjpsypqxekdqmbvvlxnuqupapimvlpeswcqcaxpcratiyobnjhwmsmkemhcdpbspphfxhtwtjngbubxzahearqgfyyaaghjkhblleyonbjuqnkkikagieaaffuoacpmhvrmpxcrebkxgctzfchzkjgvpmmbebhcexghj'
solve(A1) # time limit exceed for 


# # # Python:
# # def isPal(A):
# #     B = A[::-1]
# #     return (A == B)


# # class Solution:
# #     # @param A : string
# #     # @return an integer
# #     def solve(A):
# #         if (isPal(A)):
# #             return 1
        
# #         B = A[::-1]
        
# #         for i in range(len(A)):
# #             if (A[i] != B[i]):
                
# #                 if (i != len(A) - 1):
# #                     j = len(A) - 1 - i;
                    
# #                     word1 = A[:i] + A[i + 1:]
# #                     word2 = A[:j] + A[j + 1:]
                
# #                 else:
# #                     word1 = A[:len(A) - 1]
# #                     word2 = A[1:]
                
# #                 if (isPal(word1) or isPal(word2)):
# #                     return 1
# #                 else:
# #                     return 0
# Scala:
# class Solution {

#     def isPalindrome(A: String, left: Int, right: Int): Boolean = {
#         var left2 = left
#         var right2 = right
#         while(right2 >= left2 && A.charAt(left2) == A.charAt(right2)){
#             left2 += 1
#             right2 -= 1
#         }
#         return right2 < left2
#     }

#     def solve(A: String): Int  = {
    
#         var left: Int = 0
#         var right: Int = A.length - 1
#         while(right >= left && A.charAt(left) == A.charAt(right)){
#             left += 1
#             right -= 1
#         }
#         if(right < left || isPalindrome(A, left + 1, right) || isPalindrome(A, left, right - 1))
#             return 1
#         else
#             return 0
#     }
# }

# C++
# int Solution::solve(string A) 
# {
#     int i{},j=A.size()-1,x=-1,y=-1;
    
#     while(i<j)
#     {
#         if(A[i]==A[j])
#         {
#             i++;
#             j--;
#         }
#         else
#         {
#             x=i;
#             y=j;
#             break;
#         }
#     }
    
#     if(x==-1)
#     {
#         return 1;
#     }
    
#     i=x+1;
#     j=y;
#     bool b=false;
    
#     while(i<j)
#     {
#         if(A[i]==A[j])
#         {
#             i++;
#             j--;
#         }
#         else
#         {
#             b=true;
#             break;
#         }
#     }
    
#     if(!b)
#     {
#         return 1;
#     }
    
#     i=x;
#     j=y-1;
    
#     while(i<j)
#     {
#         if(A[i]==A[j])
#         {
#             i++;
#             j--;
#         }
#         else
#         {
#             return 0;
#         }
#     }
    
#     return 1;
# }
# GO:
# /**
#  * @input A : String
#  * 
#  * @Output Integer
#  */
# func solve(A string )  (int) {
#     l,r:=0,len(A)-1
#     n:=len(A)
#     var temp string
#     for l<=r{
#         if A[l] != A[r]{
#             temp = A[:l]
#             if l+1<n{
#                 temp += A[l+1:]
#             }
#             if temp==reverse(temp){
#                 return 1
#             }
#             temp = A[:r]
#             if r+1<n{         
#                 temp += A[r+1:]
#             }
#             if temp==reverse(temp){
#                 return 1
#             }else{
#                 return 0
#             }
#         }else{
#             l++
#             r--
#         }
#     }
#     if A==reverse(A){
#         return 1
#     }else{
#         return 0
#     }
#     return 0
# }

# func reverse(A string) string{
#     run := []rune(A)
#     l,r := 0,len(A)-1
#     for l<r{
#         run[l],run[r] = run[r],run[l]
#         l++
#         r--
#     }
#     return string(run)
# }