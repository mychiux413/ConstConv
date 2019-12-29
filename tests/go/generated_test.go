package generated

import "testing"
import "github.com/stretchr/testify/assert"

func TestGenerated(t *testing.T) {
	ml := NewMultiLangs(ZHTW)
	assert.Equal(t, "您好,歡迎", ml.Hello)
	assert.Equal(t, "登入", ml.Login)
	assert.Equal(t, "繁體中文", ml.SelectLang)
	ml.SetLang(EN)
	assert.Equal(t, "Hello,Welcome", ml.Hello)
	assert.Equal(t, "Login", ml.Login)
	assert.Equal(t, "English", ml.SelectLang)
}
