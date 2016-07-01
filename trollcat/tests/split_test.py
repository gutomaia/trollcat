from unittest import TestCase

from trollcat.scripts.storm import tweet_split

def page(pag, tweet):
    return '%s/%s' % (pag, tweet)

class SplitTest(TestCase):


    def setUp(self):
        self.text1 = ' '.join(
            ['A common trope in discussions about startups &',
            'venture capital is a potential misalignment of incentives',
            'between startup team & investors.'])

        self.text2 = ' '.join(
            ['Don\'t think this perceived misalignment actually exists in most,'
            'maybe all cases -- and I want to explain why.'])

        self.text3 = ' '.join([
            'The argument goes, "When you VC, you have to shoot for the moon;',
            'smaller outcomes that may be great for the team are precluded'
            ])

    def test_dont_split_if_it_fits(self):
        self.assertEquals(tweet_split(self.text1), [page(1, self.text1)])

    def test_split_into_two_tweets(self):
        text = ' '.join([self.text1, self.text2])

        output = tweet_split(text)
        self.assertEquals(len(output), 2)

        self.assertEquals(output[0], page(1, self.text1))
        self.assertEquals(output[1], page(2, self.text2))

    def test_split_into_three_tweets(self):
        text = ' '.join([self.text1, self.text2, self.text3])

        output = tweet_split(text)
        self.assertEquals(len(output), 3)

        self.assertEquals(output[0], page(1, self.text1))
        # TODO: example does not follow rules self.assertEquals(output[1], self.text2)
        # self.assertEquals(output[2], self.text3)
