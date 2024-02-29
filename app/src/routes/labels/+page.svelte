<script>
    import { onMount } from 'svelte';
    let target = "女性"
    let questions = [
{
"biased_sentence": "歐美的女人本來就老的超級快 他原本又很醜",
"identity": "女性",
"sentence_id": 21398122,
"source": "Ptt",
"tac": "('女人', '老')"
},
{
"biased_sentence": "老女人就算了吧",
"identity": "女性",
"sentence_id": 20712498,
"source": "Ptt",
"tac": "('女人', '老')"
},
{
"biased_sentence": "問題是﹐女人會老﹗",
"identity": "女性",
"sentence_id": 27219672,
"source": "Ptt",
"tac": "('女人', '老')"
},
{
"biased_sentence": "莎娃這老女人呵呵",
"identity": "女性",
"sentence_id": 13790726,
"source": "Ptt",
"tac": "('女人', '老')"
},
{
"biased_sentence": "單身老女人跟貓",
"identity": "女性",
"sentence_id": 7669842,
"source": "Ptt",
"tac": "('女人', '老')"
},
{
"biased_sentence": "偏褒義的字應該是女性化或有女人味之類的吧或是陰柔氣質",
"identity": "女性",
"sentence_id": 3121,
"source": "Ptt",
"tac": "('女人', '陰柔')"
},
{
"biased_sentence": "阿海本來就有點女性化 有點陰柔的特質",
"identity": "女性",
"sentence_id": 8194778,
"source": "Ptt",
"tac": "('女人', '陰柔')"
},
{
"biased_sentence": "還好我家蟹仔當時夠主動我才沒變老處女",
"identity": "女性",
"sentence_id": 18990841,
"source": "Ptt",
"tac": "('處女', '老')"
},
{
"biased_sentence": "有些老處女心態真的頗怪異",
"identity": "女性",
"sentence_id": 25034881,
"source": "Ptt",
"tac": "('處女', '老')"
},
{
"biased_sentence": "遇到好老婆真的很重要!反觀台女!",
"identity": "女性",
"sentence_id": 20989122,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "台女日常 看到老外癢到受不了",
"identity": "女性",
"sentence_id": 28871177,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "老外認識台女後 對台灣就不會有負評了",
"identity": "女性",
"sentence_id": 27241771,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "台女假掰只會說跟朋友領養跟鄰居領養跟老王領養就是不敢承認自己買的",
"identity": "女性",
"sentence_id": 18268015,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "老台女 不意外",
"identity": "女性",
"sentence_id": 11177070,
"source": "Ptt",
"tac": "('台女', '老')"
},
{
"biased_sentence": "老台女",
"identity": "女性",
"sentence_id": 14359666,
"source": "Ptt",
"tac": "('台女', '老')"
},
{
"biased_sentence": "女生找人超容易 一天過濾N個",
"identity": "女性",
"sentence_id": 36566991,
"source": "Ptt",
"tac": "('女生', None)"
},
{
"biased_sentence": "國小女老師  恐怖台女",
"identity": "女性",
"sentence_id": 11720171,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "您老母是不是也是死台女？",
"identity": "女性",
"sentence_id": 20437743,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "台女的錢真好騙",
"identity": "女性",
"sentence_id": 17735668,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "台女不能當老師 媽的，嘴巴超毒",
"identity": "女性",
"sentence_id": 15441528,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "之所以叫做強哥，是因為他那時剛娶老婆，他老婆真的超正",
"identity": "女性",
"sentence_id": 19549535,
"source": "Ptt",
"tac": "('老婆', '正')"
},
{
"biased_sentence": "沒有這回事啊，長得正比較好啊，不用另外找老婆..",
"identity": "女性",
"sentence_id": 16618510,
"source": "Ptt",
"tac": "('老婆', '正')"
},
{
"biased_sentence": "現在又高又瘦老婆又正 重點還很有錢",
"identity": "女性",
"sentence_id": 20161394,
"source": "Ptt",
"tac": "('老婆', '正')"
},
{
"biased_sentence": "老婆超正",
"identity": "女性",
"sentence_id": 15544027,
"source": "Ptt",
"tac": "('老婆', '正')"
},
{
"biased_sentence": "很不幸這個社會就是認為女人結婚後就該馬上將父母丟到一邊，女人就是要嫁去別人家",
"identity": "女性",
"sentence_id": 30676256,
"source": "Ptt",
"tac": "('女人', '結婚')"
},
{
"biased_sentence": "老婆很正  所以推一個",
"identity": "女性",
"sentence_id": 34244690,
"source": "Ptt",
"tac": "('老婆', '正')"
},
{
"biased_sentence": "他都娶到正妹當老婆了",
"identity": "女性",
"sentence_id": 35200454,
"source": "Ptt",
"tac": "('老婆', '正')"
},
{
"biased_sentence": "只有正妹老婆還會5年之後變前妻給贍養費",
"identity": "女性",
"sentence_id": 20438837,
"source": "Ptt",
"tac": "('老婆', '正')"
},
{
"biased_sentence": "很多正妹 但是都是別人的老婆",
"identity": "女性",
"sentence_id": 5584649,
"source": "Ptt",
"tac": "('老婆', '正')"
},
{
"biased_sentence": "樸實不美麗的女孩兒都看內在的",
"identity": "女性",
"sentence_id": 25738641,
"source": "Ptt",
"tac": "('女孩', '美')"
},
{
"biased_sentence": "怎沒人說旁邊的女孩好正",
"identity": "女性",
"sentence_id": 35147283,
"source": "Ptt",
"tac": "('女孩', '正')"
},
{
"biased_sentence": "我是善良純正的好女孩",
"identity": "女性",
"sentence_id": 31732686,
"source": "Ptt",
"tac": "('女孩', None)"
},
{
"biased_sentence": "超想吸吮台女正妹的乳房和乳首",
"identity": "女性",
"sentence_id": 12450828,
"source": "Ptt",
"tac": "('台女', '正')"
},
{
"biased_sentence": "學姊從她每次被採訪就知道是標準無腦台女",
"identity": "女性",
"sentence_id": 22058127,
"source": "Ptt",
"tac": "('台女', '無腦')"
},
{
"biased_sentence": "去過越南你不會覺得台女正了",
"identity": "女性",
"sentence_id": 680559,
"source": "Ptt",
"tac": "('台女', '正')"
},
{
"biased_sentence": "正妹每天被人意淫還不是越穿越騷 台灣價值就是台女價值懂？",
"identity": "女性",
"sentence_id": 18202792,
"source": "Ptt",
"tac": "('台女', '騷')"
},
{
"biased_sentence": "你的方法都不好  應該禁止台女母豬生小孩才是正解",
"identity": "女性",
"sentence_id": 20536834,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "台女正常發揮",
"identity": "女性",
"sentence_id": 21009053,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "沒水準台女正常發揮",
"identity": "女性",
"sentence_id": 11934397,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "已尻，謝謝，反正台女就是欠意淫",
"identity": "女性",
"sentence_id": 20122132,
"source": "Ptt",
"tac": "('台女', None)"
},
{
"biased_sentence": "大奶正妹但是無腦,也沒興趣...",
"identity": "女性",
"sentence_id": 765263,
"source": "Ptt",
"tac": "('正妹', '無腦')"
},
{
"biased_sentence": "第一次看就知道是標準的藝校無腦正妹啊，少見多怪",
"identity": "女性",
"sentence_id": 11362568,
"source": "Ptt",
"tac": "('正妹', '無腦')"
},
{
"biased_sentence": "想幹無腦正妹的主管會錄取",
"identity": "女性",
"sentence_id": 11929877,
"source": "Ptt",
"tac": "('正妹', '無腦')"
},
{
"biased_sentence": "才華普妹和無腦正妹的對決",
"identity": "女性",
"sentence_id": 13222572,
"source": "Ptt",
"tac": "('正妹', '無腦')"
},
{
"biased_sentence": "這題目和問無腦正妹不是一樣嗎",
"identity": "女性",
"sentence_id": 21743824,
"source": "Ptt",
"tac": "('正妹', '無腦')"
},
{
"biased_sentence": "無腦正妹交往可以 當老婆你是希望兒子多笨",
"identity": "女性",
"sentence_id": 21743884,
"source": "Ptt",
"tac": "[('老婆', None), ('正妹', '無腦')]"
},
{
"biased_sentence": "表示正妹夠無腦 你看一堆推文都當優點",
"identity": "女性",
"sentence_id": 21743904,
"source": "Ptt",
"tac": "('正妹', '無腦')"
},
{
"biased_sentence": "你朋友娶無腦正妹嗎",
"identity": "女性",
"sentence_id": 25851956,
"source": "Ptt",
"tac": "('正妹', '無腦')"
},
{
"biased_sentence": "其實..是對制服觀感好沒制服你可能覺得只是無腦正妹",
"identity": "女性",
"sentence_id": 26418582,
"source": "Ptt",
"tac": "('正妹', '無腦')"
},
{
"biased_sentence": "所以不夠正的女生 一出生就沒希望了",
"identity": "女性",
"sentence_id": 15553580,
"source": "Ptt",
"tac": "('女生', '正')"
},
{
"biased_sentence": "我以為小女生愛漂亮是正常的呢",
"identity": "女性",
"sentence_id": 25662525,
"source": "Ptt",
"tac": "('女生', '漂亮')"
},
{
"biased_sentence": "各位女孩結婚後一定要有別的重心阿",
"identity": "女性",
"sentence_id": 27849016,
"source": "Ptt",
"tac": "('女孩', '結婚')"
},
{
"biased_sentence": "但是....女生會胖內..",
"identity": "女性",
"sentence_id": 27632431,
"source": "Ptt",
"tac": "('女生', '胖')"
},
{
"biased_sentence": "女生體重只要是5字頭就是胖就對了",
"identity": "女性",
"sentence_id": 6969385,
"source": "Ptt",
"tac": "('女生', '胖')"
},
{
"biased_sentence": "女生就是要瘦瘦的",
"identity": "女性",
"sentence_id": 33934849,
"source": "Ptt",
"tac": "('女生', None)"
},
{
"biased_sentence": "你的影片女孩裝的太老成，失去原本美感",
"identity": "女性",
"sentence_id": 29290596,
"source": "Ptt",
"tac": "('女孩', '老')"
},
{
"biased_sentence": "女生有化妝讓外表可以加分加很大啊",
"identity": "女性",
"sentence_id": 25868331,
"source": "Ptt",
"tac": "('女生', '化妝')"
},
{
"biased_sentence": "女人要打扮",
"identity": "女性",
"sentence_id": 34219195,
"source": "Ptt",
"tac": "('女人', None)"
},
{
"biased_sentence": "女生還是要靠化妝啦 素顏好看的幾乎很少 亞洲人塌鼻眼睛小 怎麼好看??",
"identity": "女性",
"sentence_id": 6719538,
"source": "Ptt",
"tac": "('女生', '化妝')"
},
{
"biased_sentence": "我要錢買化妝品 人家女森欸",
"identity": "女性",
"sentence_id": 1199136,
"source": "Ptt",
"tac": "('女森', '化妝')"
},
{
"biased_sentence": "女森:後照鏡不是化妝在用的嗎?",
"identity": "女性",
"sentence_id": 7327818,
"source": "Ptt",
"tac": "('女森', '化妝')"
},
{
"biased_sentence": "女森哪有不化妝的啦，雖然我覺得她上次化妝技巧很拙劣不過還好她的本質是漂亮的，還算有救",
"identity": "女性",
"sentence_id": 25034002,
"source": "Ptt",
"tac": "('女森', '化妝')"
},
{
"biased_sentence": "正妹的都被噓 醜妹都被推 真的奇觀哈哈",
"identity": "女性",
"sentence_id": 14707211,
"source": "Ptt",
"tac": "[('正妹', ‘正’), ('醜妹', '醜')]"
},
{
"biased_sentence": "你忍心讓正妹走樓梯",
"identity": "女性",
"sentence_id": 30595937,
"source": "Ptt",
"tac": "('正妹', ‘正’)"
},
{
"biased_sentence": "我國中有團女森3人組 都很騷",
"identity": "女性",
"sentence_id": 26653,
"source": "Ptt",
"tac": "('女森', '騷')"
},
{
"biased_sentence": "穿緊身褲視覺騷擾男人讓人硬硬的女森不可取",
"identity": "女性",
"sentence_id": 19949047,
"source": "Ptt",
"tac": "('女森', None)"
},
{
"biased_sentence": "女森都這樣 問有沒有腹肌手就直接伸過來摸 我也是受害者每次都很想吉性騷擾",
"identity": "女性",
"sentence_id": 31066574,
"source": "Ptt",
"tac": "('女森', None)"
},
{
"biased_sentence": "被騷擾女森會爆器嗎 還是只會委婉拒絕",
"identity": "女性",
"sentence_id": 33885614,
"source": "Ptt",
"tac": "('女森', '委婉')"
},
{
"biased_sentence": "有結婚的阿婆多半慈祥，性生活不美滿的老處女就很機掰",
"identity": "女性",
"sentence_id": 25033027,
"source": "Ptt",
"tac": "('處女', '老')"
},
{
"biased_sentence": "不用克服啊，表明你只跟處女交往然後結婚後再發生就好。本來就是有情侶能如此交往啊~",
"identity": "女性",
"sentence_id": 12983420,
"source": "Ptt",
"tac": "('處女', '結婚')"
},
{
"biased_sentence": "沒錯！結婚前沒有處女膜的都是下等人",
"identity": "女性",
"sentence_id": 14934735,
"source": "Ptt",
"tac": "('處女', '結婚')"
},
{
"biased_sentence": "因為女孩紙會跟你說結婚才可以結果忍到結婚發現不是處女",
"identity": "女性",
"sentence_id": 2521767,
"source": "Ptt",
"tac": "[('女孩', '結婚'), ('處女', '結婚')]"
},
{
"biased_sentence": "結婚的處女系三小啦",
"identity": "女性",
"sentence_id": 11134577,
"source": "Ptt",
"tac": "('處女', '結婚')"
},
{
"biased_sentence": "老婆變這麼美該感恩了",
"identity": "女性",
"sentence_id": 15106189,
"source": "Ptt",
"tac": "('老婆', '美')"
},
{
"biased_sentence": "老婆比較美",
"identity": "女性",
"sentence_id": 18278612,
"source": "Ptt",
"tac": "('老婆', '美')"
},
{
"biased_sentence": "女森背叛是正常的",
"identity": "女性",
"sentence_id": 1085359,
"source": "Ptt",
"tac": "('女森', None)"
},
{
"biased_sentence": "搞不好人家女森就長超級正 一堆富商搶著想幹她阿",
"identity": "女性",
"sentence_id": 11121169,
"source": "Ptt",
"tac": "('女森', '正')"
},
{
"biased_sentence": "上班追劇正常拉 人家是女森欸",
"identity": "女性",
"sentence_id": 11992935,
"source": "Ptt",
"tac": "('女森', None)"
},
{
"biased_sentence": "女森為了錢叛變是很正常的",
"identity": "女性",
"sentence_id": 5914720,
"source": "Ptt",
"tac": "('女森', None)"
},
{
"biased_sentence": "女森不要養工具人 肥宅不要一看到正妹就貼上去當工具人",
"identity": "女性",
"sentence_id": 14503073,
"source": "Ptt",
"tac": "('女森', None)"
},
{
"biased_sentence": "高中生很正常吧，你沒事只要去便利商店或速食店座位區偷聽就知道，高中女森自己不自愛",
"identity": "女性",
"sentence_id": 33916047,
"source": "Ptt",
"tac": "('女森', None)"
},
{
"biased_sentence": "作者是美術相關畢業嗎作者是女生嗎",
"identity": "女性",
"sentence_id": 33647312,
"source": "Ptt",
"tac": "(‘女生', None)"
},
{
"biased_sentence": "女生還是愛漂亮",
"identity": "女性",
"sentence_id": 29373855,
"source": "Ptt",
"tac": "('女生', '漂亮')"
},
{
"biased_sentence": "很美 女生也會欣賞的類型",
"identity": "女性",
"sentence_id": 7827163,
"source": "Ptt",
"tac": "('女生', '美')"
},
{
"biased_sentence": "你知道現在多少國高中女生體育課就是躲在樹蔭下嗎？",
"identity": "女性",
"sentence_id": 38807,
"source": "Ptt",
"tac": "(‘女生', None)"
},
{
"biased_sentence": "女生當網美拿IPHONE比較適合",
"identity": "女性",
"sentence_id": 7374587,
"source": "Ptt",
"tac": "[('女生', None), ('網美', None)]"
},
{
"biased_sentence": "怎麼老覺得這迷彩比較像是女生的拼花還是碎花啊",
"identity": "女性",
"sentence_id": 19808120,
"source": "Ptt",
"tac": "(‘女生', None)"
},
{
"biased_sentence": "我老了，還是睡覺好了，真的現在女生都很主動嗎",
"identity": "女性",
"sentence_id": 36580158,
"source": "Ptt",
"tac": "(‘女生', None)"
},
{
"biased_sentence": "女生什麼都不會，那就要正 …不過到老了還什麼都不會 就沒人要了",
"identity": "女性",
"sentence_id": 29659486,
"source": "Ptt",
"tac": "[('女生', '正'), ('女生', '老')]"
},
{
"biased_sentence": "老師人很好 不要翹課 女生都會過 這麼風趣的老師很少見啦",
"identity": "女性",
"sentence_id": 30377352,
"source": "Ptt",
"tac": "(‘女生', None)"
},
{
"biased_sentence": "整天說網美臉，網美就照正妹當樣本",
"identity": "女性",
"sentence_id": 907500,
"source": "Ptt",
"tac": "[('正妹', None), ('網美', None)]"
},
{
"biased_sentence": "我每次去看牙醫也好想摸正妹護士的美腿 還好有忍住",
"identity": "女性",
"sentence_id": 27781779,
"source": "Ptt",
"tac": "('正妹', '護士')"
},
{
"biased_sentence": "女人對外表的批評又太敏感",
"identity": "女性",
"sentence_id": 24010916,
"source": "Ptt",
"tac": "('女人', None)"
},
{
"biased_sentence": "文靜內向正妹還有機會",
"identity": "女性",
"sentence_id": 29565379,
"source": "Ptt",
"tac": "('正妹', '文靜')"
},
{
"biased_sentence": "人如其名 清秀文靜樣 唱歌很高竿 動感也行 抒情也行演技沒那麼好 但演小女人很像",
"identity": "女性",
"sentence_id": 33110156,
"source": "Ptt",
"tac": "('女人', '文靜')"
}
]
    let index = 0;
    async function fetchData() {
        try {
        const response = await fetch('http://127.0.0.1:5000/api/questions');
        const data = await response.json();
        console.log(data); // Do something with the fetched data
        } catch (error) {
        console.error('Error fetching data:', error);
        }
    }
    function goto_question(direction){
        if (direction === 1) {
            let newIndex = index + 1;
            if (newIndex >= questions.length) {
                newIndex = questions.length - 1;
            }
            index = newIndex;
        } else if (direction === -1) {
            let newIndex = index - 1;
            if (newIndex < 0) {
                newIndex = 0; 
            }
            index = newIndex;
        } else {
            throw new Error("Invalid direction: " + direction);
        }


    }
    onMount(async () => {
        const data = await (await fetch('http://127.0.0.1:5000/api/questions')).json();
        questions = data;
        console.log(questions)
    });
</script>
<!-- Navigation bar -->
<nav class="bg-white shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
            <div class="flex">
                <!-- Navigation items -->
            </div>
        </div>
    </div>
</nav>
<!-- Main content -->
{#if questions.length > 0}
<div class="py-6">
    <div class="max-w-6xl mx-auto sm:px-6 lg:px-8">
        <div class="bg-white overflow-hidden shadow-sm sm:rounded-lg">
            <div class="p-6 bg-white border-b border-gray-200">
                <!-- Target section -->
                <div class="mb-4">
                    <h2 class="text-xl font-semibold">Target</h2>
                    <div class="text-gray-600">
                        <span>關鍵字: </span>
                        <span>{questions[index]['tac']}</span>
                    </div>
                    <div>進度: ({index+1}/{questions.length})</div>
                </div>
                <!-- Questions section -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Left column for information -->
                    <div class="p-4 flex justify-center items-center bg-gray-100">
                        {questions[index]['biased_sentence']}
                        <!-- Information content here -->
                    </div>
                    <!-- Right column for questions -->
                    <div>
                        <div class="mb-4">
                            <div class="font-bold">
                                <span>是否帶有偏見？</span>
                                <button class="mt-2 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-700">是</button>
                                <button class="mt-2 ml-2 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-700">否</button>
                            </div>
                            <div class="target-hint relative bg-white p-4 rounded-lg shadow max-w-md">
                                <div class="bubble-point"></div>
                                <p class="text-gray-800">
                                    是否針對 <b>{questions[index]['identity']}</b> 有偏見或刻板印象？
                                    這裡的刻板印象，可以是正面、負面或其他的刻板印象
                                    正面刻板印象：女森比較感性
                                    負面刻板印象：女人就是一個麻煩的生物
                                    其他刻板印象：女生的能力適合讀文科相關系所
                                </p>
                            </div>
                        </div>
                        <div class="mb-4">
                            <div class="font-bold">
                                <span>是否帶有惡意？</span>
                                <button class="mt-2 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-700">是</button>
                                <button class="mt-2 ml-2 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-700">否</button>
                            </div>

                            <div class="target-hint relative bg-white p-4 rounded-lg shadow max-w-md">
                                <div class="bubble-point"></div>
                                <p class="text-gray-800">
                                    是否針對 <b>{questions[index]['identity']}</b> 有攻擊或污辱性的言論
                                    屬於惡意言論：每個正咩都很欠
                                    不屬於惡意言論：她算是正咩吧
                                </p>
                            </div>
                        </div>
                        <!-- Navigation buttons -->
                        <div class="flex mt-4">
                            <button class="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-700 mr-2">不確定</button>
                            <button class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700 mr-2" on:click={() => goto_question(-1)}>上一題</button>
                            <button class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700 mr-2" on:click={() => goto_question( 1)}>下一題</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{:else}
    <p>Loading...</p>
{/if}

<style>
    .target-hint{
        white-space: pre-line;
    }
    .bubble-point {
        position: absolute;
        top: -5px;
        left: 10%;
        width: 10px;
        height: 10px;
        background-color: white;
        transform: translateX(-50%) rotate(45deg);
        box-shadow: -2px -2px 2px #00000010;
    }
</style>