<?php

/* display/export/hidden_inputs.twig */
class __TwigTemplate_9c96fba511506a039cda6b5b8f0f120d9efd931f23824e86e18df68e53a52143 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        if (((isset($context["export_type"]) ? $context["export_type"] : null) == "server")) {
            // line 2
            echo "    ";
            echo PhpMyAdmin\Url::getHiddenInputs("", "", 1);
            echo "
";
        } elseif ((        // line 3
(isset($context["export_type"]) ? $context["export_type"] : null) == "database")) {
            // line 4
            echo "    ";
            echo PhpMyAdmin\Url::getHiddenInputs((isset($context["db"]) ? $context["db"] : null), "", 1);
            echo "
";
        } else {
            // line 6
            echo "    ";
            echo PhpMyAdmin\Url::getHiddenInputs((isset($context["db"]) ? $context["db"] : null), (isset($context["table"]) ? $context["table"] : null), 1);
            echo "
";
        }
        // line 8
        echo "
";
        // line 10
        if ( !twig_test_empty((isset($context["single_table"]) ? $context["single_table"] : null))) {
            // line 11
            echo "    <input type=\"hidden\" name=\"single_table\" value=\"TRUE\">
";
        }
        // line 13
        echo "
<input type=\"hidden\" name=\"export_type\" value=\"";
        // line 14
        echo twig_escape_filter($this->env, (isset($context["export_type"]) ? $context["export_type"] : null), "html", null, true);
        echo "\">

";
        // line 17
        echo "<input type=\"hidden\" name=\"export_method\" value=\"";
        echo twig_escape_filter($this->env, (isset($context["export_method"]) ? $context["export_method"] : null), "html", null, true);
        echo "\">

";
        // line 19
        if ( !twig_test_empty((isset($context["sql_query"]) ? $context["sql_query"] : null))) {
            // line 20
            echo "    <input type=\"hidden\" name=\"sql_query\" value=\"";
            echo twig_escape_filter($this->env, (isset($context["sql_query"]) ? $context["sql_query"] : null), "html", null, true);
            echo "\">
";
        }
        // line 22
        echo "
<input type=\"hidden\" name=\"template_id\" value=\"";
        // line 23
        echo twig_escape_filter($this->env, (isset($context["template_id"]) ? $context["template_id"] : null), "html", null, true);
        echo "\">
";
    }

    public function getTemplateName()
    {
        return "display/export/hidden_inputs.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  74 => 23,  71 => 22,  65 => 20,  63 => 19,  57 => 17,  52 => 14,  49 => 13,  45 => 11,  43 => 10,  40 => 8,  34 => 6,  28 => 4,  26 => 3,  21 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "display/export/hidden_inputs.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/display/export/hidden_inputs.twig");
    }
}
